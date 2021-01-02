import requests
from bs4 import BeautifulSoup

URL = 'https://online.stanford.edu/search-catalog'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}


def parse():
    r = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(r.text, 'html.parser')
    items = soup.findAll('a', class_='node node--type-course')

    courses = []


    for item in items:
#Error
        courses.append({
                'title': item.find('h3').text,
                'url': URL + item.get('href')
            })
        print(courses)
        for course in courses:

            print(course['title'], course['url'])
parse()

