from bs4 import BeautifulSoup
import requests

header = {'user-agent': 'mozilla/5.0 (Windows NT 10.0;Win64;x64)\
          AppleWebKit/537.36(KHTML,like gecko)\
            chrome/58.0.3029.110 safari/537.3'}

def current_weather(city):
    city = city.replace(" ","+")
    res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome..69i57.4199j0j1&sourceid=chrome&ie=UTF-8',headers= header)
    
    print("searching............\n")
    soup = BeautifulSoup(res.text,'html.parser')
    # location = soup.select('#wob_loc')[0].getText().strip()
    # time = soup.select('#wob_dts')[0].getText().strip()
    # info = soup.select('#wob_dc')[0].getText().strip()
    # weather = soup.select('#wob_tm')[0].getText().strip()


    # print(location)
    # print(time)
    # print(info)
    # print(weather+"C")


    print(soup)
city = input("enter the city name")
city = city + "weather"
current_weather(city)
