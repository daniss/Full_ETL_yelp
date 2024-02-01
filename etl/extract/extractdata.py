import requests as requests
#from fake_useragent import UserAgent
from bs4 import BeautifulSoup

def finder(i, loc):
    url = f"https://www.yelp.fr/search?find_desc=Restaurants&find_loc={loc}&start={i}"
    headers = {'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser') 
    test_end = soup.find('h3', class_='css-oxqmph')
    try:
        if test_end.text == "Nous sommes désolés, la page de résultats que vous avez demandée n'est pas disponible.":
            return response.status_code
    except:
        pass
    names = soup.find_all('div', class_="container__09f24__FeTO6 hoverable__09f24___UXLO css-65wjx3")
    restaurants = []
    for name in names:
        restaurants.append(name.text)
    return restaurants

def scrape():
    localisations = ["Paris", "Marseille", "Lyon", "Toulouse", "Nice", "Nantes", "Montpellier", "Strasbourg", "Bordeaux", "Lille"]
    f = open("data.json", "w")
    i = 0
    for localisation in localisations:
        while True:
            restaurants = finder(i, localisation)
            if type(restaurants) is int or i == 20:
                break
            for restaurant in restaurants:
                f.write(f"Ville : {localisation} et {restaurant} + \n")
            i += 10
        i = 0
    f.close()
