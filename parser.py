import requests
from bs4 import BeautifulSoup
import csv
URL = 'https://online.stanford.edu/search-catalog'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
CSV = 'courses.csv'


def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.findAll('a', class_='node node--type-course')

    courses = []


    for item in items:

        courses.append({
                'title': item.find('h3').get_text(strip=True),
                'url': URL + item.get('href')
           })
    #for course in courses:


    return courses



def save(items, path):
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(['Название курса', 'Ссылка'])
        for item in items:
            writer.writerow([item['title'], item['url']])





def pages():
    max_pages = input("Enter the number of pages: ")
    max_pages = int(max_pages.strip())
    html = get_html(URL)

    if html.status_code == 200:
        courses = []
        for page in range(0, max_pages+1):
            print(f'Parsing {page} page')
            html = get_html(URL, params={'page':page})

            courses.extend(get_content(html.text))
            save(courses, CSV)

    else:
        print('Error')


pages()

