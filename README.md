# Weathr 
A fast, lightweight command-line weather tool powered by NOAA and OpenStreetMap — no API key required.
Get accurate forecasts and open the radar for any location instantly.

---

## ✨ Features
🌎 Search weather by city, state, ZIP code, or place name

🌡️ Current temperature, wind, and conditions

🛰️ One-click radar view in your browser

🔌 No API keys, no accounts, no tracking

🖥️ Works on Windows, macOS, and Linux

⚡ Simple, fast, and open-source

---

## 📦 Installation
**You have 2 options here:**
### Option 1 *(The Easy Way)*:

Download the .exe file from the latest release

### Option 2 *(The Hard Way)*:

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Weathr.git
cd Weathr
Install dependencies:
```

```bash
pip install requests
🚀 Usage
Run the script:
```

```bash
python weather.py
You will be prompted for a location:
```

```Code
=== Weathr CLI ===
Enter a location: montgomery
Example output:
```

```Code
Weather for Montgomery, Alabama, United States
----------------------------------------------
Temperature: 58°F
Wind: 5 mph NW
Conditions: Mostly Clear
Radar URL: https://radar.weather.gov/?center=KMXX
You will then be asked if you want to open the radar in your browser.
```

---

## 🧠 How It Works
1. Geocoding  
Uses OpenStreetMap Nominatim to convert your location into latitude/longitude.

2. Weather Data  
Queries NOAA's Weather API to retrieve the nearest forecast office and current conditions.

3. Radar  
Opens the live NOAA radar viewer centered on the nearest radar station.

---

## 📁 Project Structure
```Code
Weathr/
│
├── weather.py
├── README.md
└── .gitignore
```

---

## 🧰 Requirements
### Python 3.8+
---
### requests library

Install with:
```bash
pip install requests
```

---

## 🛣️ Roadmap
[ ] Hourly forecast option

[ ] Metric/imperial toggle

[ ] JSON output mode

[ ] PyPI package (pip install weathr)

[ ] Better radar centering (NOAA limitations)

---

## 🤝 Contributing
Pull requests are welcome!
If you find a bug or want a feature added, open an issue.

##📜 License
MIT License — free to use, modify, and distribute.
