import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import requests
from geopy.geocoders import Nominatim
from dotenv import load_dotenv
import os
import requests
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from geopy.geocoders import Nominatim

load_dotenv()  # Load environment variables

OPENCAGE_API_KEY = os.getenv("OPENCAGE_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


# Function to get the current IP address location (latitude, longitude)
def get_current_location():
    try:
        response = requests.get("http://ipinfo.io")
        data = response.json()
        loc = data['loc'].split(',')
        lat = float(loc[0])
        lon = float(loc[1])
        city = data['city']
        region = data['region']
        country = data['country']
        return lat, lon, city, region, country
    except Exception as e:
        print(f"Error getting location: {e}")
        return None, None, None, None, None

# Function to get the address from latitude and longitude using Nominatim
def get_address_from_coords(lat, lon):
    try:
        geolocator = Nominatim(user_agent="myGeocoder")
        location = geolocator.reverse((lat, lon), language='en')
        return location.address if location else "Address not found"
    except Exception as e:
        print(f"Error fetching address using Nominatim: {e}")
        return None

# Function to get the address from latitude and longitude using OpenCage Geocoder
def get_address_from_coords_opencage(lat, lon):
    try:
        url = f"https://api.opencagedata.com/geocode/v1/json?q={lat}+{lon}&key={api_key}"
        response = requests.get(url)
        data = response.json()
        
        if data['results']:
            return data['results'][0]['formatted']
        else:
            return "Address not found"
    except Exception as e:
        print(f"Error fetching address using OpenCage: {e}")
        return None

# Function to get weather data based on latitude and longitude
def get_weather(lat, lon):
    try:
        
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        
        if data["cod"] == 200:
            main = data["main"]
            weather = data["weather"][0]
            temperature = main["temp"]
            description = weather["description"]
            return temperature, description
        else:
            return None, None
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None, None

phone_number = input("Enter a phone number (with country code, e.g., +91 000000000): ")
number = phonenumbers.parse(phone_number)

region = geocoder.description_for_number(number, "en")
service_provider = carrier.name_for_number(number, "en")
valid = phonenumbers.is_valid_number(number)
timeZone = timezone.time_zones_for_number(number)
lat, lon, city, region_location, country = get_current_location()

#
print(f"Phone Number: {phone_number}")
print(f"Service Provider: {service_provider}")
print(f"Region: {region}")
print(f"Valid Number: {valid}")
print(f"Time Zones: {timeZone}")
print(f"Current Location: {city}, {region_location}, {country}")
print(f"Latitude: {lat}, Longitude: {lon}")

# Get the full address using Nominatim
address_nominatim = get_address_from_coords(lat, lon)
if address_nominatim:
    print(f"Full Address (Nominatim): {address_nominatim}")
else:
    # Fallback to OpenCage if Nominatim fails
    address_opencage = get_address_from_coords_opencage(lat, lon)
    print(f"Full Address (OpenCage): {address_opencage}")

# Fetch weather for the current location
temperature, description = get_weather(lat, lon)
if temperature and description:
    print(f"Current Weather: {description} with a temperature of {temperature}°C")
else:
    print("Weather data not available")
