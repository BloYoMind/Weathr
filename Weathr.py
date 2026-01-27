import requests
import webbrowser

NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"
NOAA_POINTS_URL = "https://api.weather.gov/points/{lat},{lon}"

HEADERS = {
    "User-Agent": "WeatherCLI (https://github.com/yourname/weather-cli)"
}

def geocode_location(location):
    params = {
        "q": location,
        "format": "json",
        "limit": 1
    }
    response = requests.get(NOMINATIM_URL, params=params, headers=HEADERS, timeout=10)
    response.raise_for_status()
    data = response.json()

    if not data:
        raise ValueError(f"Location not found: {location}")

    return float(data[0]["lat"]), float(data[0]["lon"]), data[0]["display_name"]


def get_noaa_forecast(lat, lon):
    points_url = NOAA_POINTS_URL.format(lat=lat, lon=lon)
    points_response = requests.get(points_url, headers=HEADERS, timeout=10)
    points_response.raise_for_status()
    points_data = points_response.json()

    forecast_url = points_data["properties"]["forecast"]
    radar_station = points_data["properties"]["radarStation"]

    forecast_response = requests.get(forecast_url, headers=HEADERS, timeout=10)
    forecast_response.raise_for_status()
    forecast_data = forecast_response.json()

    periods = forecast_data["properties"]["periods"]
    current = periods[0]

    return {
        "temperature": current["temperature"],
        "unit": current["temperatureUnit"],
        "wind": current["windSpeed"],
        "conditions": current["shortForecast"],
        "radar_station": radar_station
    }


def main():
    print("=== Weather CLI ===")
    location = input("Enter a location: ").strip()

    if not location:
        print("No location entered.")
        return

    try:
        lat, lon, display_name = geocode_location(location)
        weather = get_noaa_forecast(lat, lon)

        print(f"\nWeather for {display_name}")
        print("-" * (len(display_name) + 12))
        print(f"Temperature: {weather['temperature']}°{weather['unit']}")
        print(f"Wind: {weather['wind']}")
        print(f"Conditions: {weather['conditions']}")

        radar_url = f"https://radar.weather.gov/?center={weather['radar_station']}"
        print(f"Radar URL: {radar_url}\n")

        choice = input("Open radar in browser? (y/n): ").strip().lower()
        if choice == "y":
            webbrowser.open(radar_url)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
