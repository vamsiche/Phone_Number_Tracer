# Phone Number Tracer

## About

This is a Python-based utility that extracts basic information from a phone number and combines it with location and weather data.

The program takes a phone number as input and displays details such as region, service provider, time zones, current location (via IP), full address, and weather.

---

## Features

* Parse and validate phone numbers
* Identify telecom carrier and region
* Fetch time zone information
* Detect current location using IP address
* Convert coordinates into readable address
* Retrieve current weather data

---

## Tech Stack

* Python
* phonenumbers (number parsing and validation)
* requests (API calls)
* geopy (reverse geocoding)
* python-dotenv (environment variables)

---

## APIs Used

* OpenCage Geocoder (fallback for address)
* OpenWeatherMap (weather data)
* ipinfo.io (IP-based location)

---

## Setup

### Install dependencies

```bash id="m9x7zp"
pip install phonenumbers requests geopy python-dotenv
```

---

### Configure environment variables

Create a `.env` file:

```env id="q8h2yx"
OPENCAGE_API_KEY=your_api_key
WEATHER_API_KEY=your_api_key
```

---

## Run the program

```bash id="z7n1vt"
python main.py
```

Enter a phone number with country code:

```id="w6c3pd"
+91XXXXXXXXXX
```

---

## Output

The program displays:

* Phone number validity
* Service provider
* Region
* Time zones
* Current IP-based location
* Latitude and longitude
* Full address
* Weather information

---

## Limitations

* Does not track real-time location of a phone number
* Location is based on IP, not the phone number itself
* Accuracy of IP-based location may vary
* Requires internet connection and API keys

---

## Learning Outcomes

* Working with third-party APIs
* Handling JSON responses
* Using environment variables securely
* Basic error handling in Python

---

## Improvements

* Fix API key variable usage in code
* Improve input validation
* Add proper exception handling
* Build a simple UI (CLI improvements or web app)

---

## Note

This project is for learning purposes only.
It does not provide real-time tracking of phone numbers.
