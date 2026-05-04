# 📱 Phone Number Info + Location + Weather (Python Project)

## 👨‍💻 About this project

This is a simple Python project I made to practice working with APIs and libraries.

It takes a phone number as input and gives:

* basic details about the number
* current location using IP
* full address using geocoding
* current weather of that location

---

## 🔧 What I used

* `phonenumbers` → to get info about phone number
* `geopy` → to convert latitude & longitude into address
* `requests` → to call APIs
* `dotenv` → to store API keys safely

APIs used:

* OpenCage (for address if fallback needed)
* OpenWeatherMap (for weather)

---

## 📂 How to run

### Step 1: Install libraries

```bash
pip install phonenumbers geopy requests python-dotenv
```

---

### Step 2: Create `.env` file

Create a file named `.env` and add:

```
OPENCAGE_API_KEY=your_key_here
WEATHER_API_KEY=your_key_here
```

---

### Step 3: Run the program

```bash
python main.py
```

Enter phone number like:

```
+91XXXXXXXXXX
```

---

## 📌 What it shows

* Phone number validity
* Service provider
* Region
* Time zones
* Your current location (via IP)
* Full address
* Weather info

---

## ⚠️ Problems / Limitations

* Location from IP is not always accurate
* Nominatim may fail sometimes (that’s why OpenCage fallback is used)
* Needs internet connection
* API keys are required

---

## 🧠 What I learned

* How to use external APIs
* How to handle JSON responses
* Basics of environment variables
* Error handling in Python

---

## 🚧 Future improvements

* Fix API key variable bug in code
* Add GUI (maybe using Tkinter or web app)
* Improve error handling
* Allow tracking based on number (currently not possible accurately)

---

## 📎 Note

This project is only for learning purpose.
It does NOT track real-time location of a phone number.

---

## ⭐ If you like it

Feel free to fork or improve it 🙂
