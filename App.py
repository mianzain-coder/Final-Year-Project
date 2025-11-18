from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

API_KEY = "ea06db0c76734a4f92f113157251411"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/weather", methods=["POST"])
def weather():
    city = request.form.get("city")
    if not city:
        return jsonify({"error": "Please enter a city name."})

    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=yes"
    response = requests.get(url)
    data = response.json()

    if "error" in data:
        return jsonify({"error": data["error"]["message"]})

    now = datetime.now()
    day = now.strftime("%A")  # e.g., Monday
    date = now.strftime("%d %B %Y")  # e.g., 14 November 2025

    weather_data = {
        "location": f"{data['location']['name']}, {data['location']['country']}",
        "temperature_c": data["current"]["temp_c"],
        "condition": data["current"]["condition"]["text"],
        "icon": data["current"]["condition"]["icon"],
        "humidity": data["current"]["humidity"],
        "wind_kph": data["current"]["wind_kph"],
        "day": day,
        "date": date
    }

    return jsonify(weather_data)


if __name__ == "__main__":
    app.run(debug=True)
