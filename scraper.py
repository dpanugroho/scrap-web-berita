import requests
from bs4 import BeautifulSoup 
import ast


def get_news_tempo(url, headers):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    for div in soup.findAll('div', {'class': 'artikel'}):
        for p in div.findAll('p'):
            return p.text
    
def get_news_kompas(url, headers):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    artikel = []
    for div in soup.findAll('div', {'class': 'read__content'}):
        temp = []
        for p in div.findAll('p'):
            temp.append(p.text)
        artikel.append(temp)
        if len(artikel)>0:
            artikel=artikel[0]
    return "".join(artikel)

def get_news_detik(url, headers):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    for div in soup.findAll('div', {'id': 'detikdetailtext'}):
        #print(div.text)
        return (div.text)

def get_news_metrotvnews(url, headers):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    for div in soup.findAll('div', {'class': 'tru'}):
        return(div.text)

def get_news_suara(url, headers):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    for div in soup.findAll('div', {'id' : 'detikdetailtext'}):
        return(div.text)

def get_news_sindo(url, headers):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    for div in soup.findAll('div', {'id':'content'}):
        return (div.text)



