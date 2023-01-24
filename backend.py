import requests
api = '0676e0efb89801f4e5442f4940707bdf'


def get_data(place, forecast=1, type_data='Temperature'):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api}"
    req = requests.get(url)
    data = req.json()
    # each forecast day has 8 readings
    data_filtered = data['list'][:forecast * 8]
    return data_filtered


if __name__ == '__main__':
    test = get_data(place="Tokyo")
    # print(test)
    # temps = [dict['main']['temp'] for dict in test]