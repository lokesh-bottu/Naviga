
import json

def get_data():
    data = open('restaurants.json')
    return json.load(data)


def get_count(data):
    country_count ={}
    for rest in data:
        country = rest['Country']
        country_count[country] = country_count.get(country,0)+1
    return country_count


def display_count(country_count):
    for item in country_count.items():
        print(item)


def get_city_count(data):
    city_count = {}
    for rest in data:
        country = rest['Country']
        city = rest['City']
        if(country in city_count.keys()):
            city_count[country][city] = city_count[country].get(city,0)+1
        else:
            city_count[country] ={}
            city_count[country][city]=1
    return city_count

def display_city_count(PerCity):
    for item in PerCity.items():
        print(item)



data = get_data()
country_count = get_count(data)
display_count(country_count)
PerCity = get_city_count(data)
display_city_count(PerCity)