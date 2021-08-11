import os
import json
import requests
from bs4 import BeautifulSoup


def get_workana_page():
    response = requests.get('https://www.workana.com/jobs?has_few_bids=1&language=pt&publication=1d')
    soup = BeautifulSoup(response.content, 'html.parser')
    tags = soup.find_all('span', title=True, class_=False)

    title_tags = soup.find_all('span', title=True, class_=False)
    delay_tags = soup.find_all('h5', class_='date')
    flag_tags = soup.find_all('span', class_='label')

    titles = list(map(lambda x: x['title'], title_tags))
    links = list(map(lambda x: 'https://www.workana.com/' + x.parent['href'], title_tags))
    delay = list(map(lambda x: str(x.strong.string), delay_tags))

    return titles


def write_json(data):
    path = os.getcwd()
    with open(path+'\data.json', 'w') as file:
        json.dump(data, file)


def read_json():
    with open('data.json') as file:
        data = json.load(file)
    return data


if __name__ == '__main__':
    titles = get_workana_page()
    write_json(titles)
    titles = read_json()