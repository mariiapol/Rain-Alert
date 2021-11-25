from twilio.rest import Client
import os
import requests

api_key = "**********"

# Set environment variables
os.environ["account_sid"] = "*************"
os.environ["auth_token"] = "**************"


# Get environment variables
account_sid = os.environ["account_sid"]
auth_token = os.environ["auth_token"]

parameters = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()

if_rain = False
for hour in weather_data["hourly"][:12]:
    id = int(hour["weather"][0]["id"])

    if id < 700:
        if_rain = True

if if_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. Bring an umbrella 🌂.",
        from_="Your Twilio number",
        to="Your mobile number"
    )

    print(message.status)

print(os.environ['PATH'])

