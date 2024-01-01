from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your OpenWeatherMap API key
api_key = "a0b41a620edf86d249d4602f8ee2195a"

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = {}
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather(city)
    return render_template('index.html', weather_data=weather_data)

def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # You can change units to 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    weather = {
        "city": city,
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
    }
    return weather

if __name__ == '__main__':
    app.run(debug=True)