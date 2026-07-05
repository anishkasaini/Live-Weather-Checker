from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv
load_dotenv()



app = Flask(__name__)

API_KEY = os.getenv("API_KEY")


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        city = request.form["city"]

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)

        data = response.json()

       
        if response.status_code == 200:

            city_name = data["name"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]
            description = data["weather"][0]["description"]

            return render_template(
                "report.html",
                city=city_name,
                temperature=temperature,
                humidity=humidity,
                wind=wind,
                description=description
            )

        else:

            error = "City not found. Please enter a valid city."

            return render_template("index.html", error=error)

    return render_template("index.html")


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)





