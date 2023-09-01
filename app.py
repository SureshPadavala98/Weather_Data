from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather(city):
    key = '4a2b6fcfdb6c2f0ca2448135dacb9602'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={key}'
    res = requests.get(url).json()
    return res

@app.route('/', methods=['GET', 'POST'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather(city)

        if weather_data['cod'] == '404':
            return render_template('weather.html', error='Enter the correct city')
        else:
            return render_template('weather.html', weather=weather_data)
    else:
        return render_template('weather.html')

if __name__ == '__main__':
    app.run(debug=True)
