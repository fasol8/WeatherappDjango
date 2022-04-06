from django.shortcuts import render
import requests
import datetime


def index(request):
    try:
        if 'city' in request.POST:
            city = request.POST['city']
        else:
            city = ''

        appid = '45541d49d6c7728b79bb57cc6b29979f'
        URL = 'https://api.openweathermap.org/data/2.5/weather'
        PARAMS = {'q': city, 'appid': appid, 'units': 'metric', 'lang': 'es'}
        r = requests.get(url=URL, params=PARAMS)
        res = r.json()
        x = datetime.datetime.now()
        data = {
            "name": res["name"],
            "temp": res["main"]["temp"],
            "feels": res["main"]["feels_like"],
            "tmax": res["main"]["temp_max"],
            "tmin": res["main"]["temp_min"],
            "coordinate": str(res["coord"]["lon"]) + " , " + str(res["coord"]["lat"]),
            "pressure": res["main"]["pressure"],
            "humidity": res["main"]["humidity"],
            "ws": res["wind"]["speed"],
            "wd": res["wind"]["deg"],
            "wg": res["wind"]["gust"],
            "description": res["weather"][0]["description"],
            "icon": res["weather"][0]["icon"],
            "sunrise": res["sys"]["sunrise"],
            "sunset": res["sys"]["sunset"],
            "cloud": res["clouds"]["all"],
            "dt": res["dt"],
            "day":x.strftime('%a %H:%M')
        }
        # print(res)
        # print(data)
        return render(request, 'weatherapp/index.html', data)
    except:
        err = "Revisa la escritura de la ciudad"

        return render(request, 'weatherapp/index.html', {'err': err})
