import requests
api = '0676e0efb89801f4e5442f4940707bdf'


def get_data(place, forecast=1, type_data='Temperature'):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api}"
    req = requests.get(url)
    data = req.json()

    match type_data:
        case 'Temperature':
            for i in range(forecast-1):
                data['list'][i]['main']

    return data['list'][0]['main']


if __name__ == '__main__':
    test = get_data(place="London")
    print(test)