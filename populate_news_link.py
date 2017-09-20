# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 06:30:54 2017

@author: dwipr
"""
import requests
from bs4 import BeautifulSoup 
import pandas as pd
import time
import numpy as np
import news_utils
from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def generate_datetime(start_month, end_month, year, news_site_name):
    date_all = []
    sep = news_utils.date_separator[news_site_name]
    start_date = date(year, start_month, 1)
    
    if (end_month == 12):
        year=year+1
    
    end_date = date(year, (end_month+1)%12, 1)
    for single_date in daterange(start_date, end_date):
      if news_site_name=='detik':
        date_all.append(single_date.strftime("%d"+sep+"%m"+sep+"%Y"))
      elif news_site_name=='suara':
      	date_all.append(single_date.strftime("%m"+sep+"%d"+sep+"%Y"))
      else:
        date_all.append(single_date.strftime("%Y"+sep+"%m"+sep+"%d"))
#      print (single_date.strftime("%Y"+sep+"%m"+sep+"%d"))
    return date_all

def get_link_kompas(datetime):
    news_urls = []
    dates = []
    for i in range(len(datetime)):
        response = requests.get('http://indeks.kompas.com/news/'+datetime[i])
        soup = BeautifulSoup(response.text, 'html.parser')
    
        for paging in soup.findAll('div', {'class': 'paging__wrap clearfix'}):
            for a in paging.findAll('a', {'class': 'paging__link paging__link--prev'}):
                last = int(a['data-ci-pagination-page'])+1
                temp = []
                for j in range(1,last):
                    response_ = requests.get('http://indeks.kompas.com/news/'+datetime[i]+'/'+str(j))
                    soup_ = BeautifulSoup(response_.text, 'html.parser')
                    for div in soup_.findAll('div', {'class': 'latest--indeks mt2 clearfix'}):
                        for a_ in div.findAll('a', {'class': 'article__link'}):
                            temp.append(a_['href'])
                news_urls.append(temp)
                dates.append(datetime[i])
        print(datetime[i])
    return dates, news_urls

def get_link_tempo(datetime):
    news_urls=[]
    dates = []
    for i in range(len(datetime)):
        # add ramdom sleep
        time.sleep(np.random.randint(1,3)) 
        response = requests.get('http://www.tempo.co/indeks/'+datetime[i])
        soup = BeautifulSoup(response.text, 'html.parser')
        temp = []
        for ul in soup.findAll('ul', {'class': 'list-terkini'}):
          for li in ul.findAll('li'):
            for div in li.findAll('div', {'class': 'box-gambar'}):
              for a in div.findAll('a'):
                temp.append(a['href'])
        news_urls.append(temp)
        dates.append(datetime[i])
        print (datetime[i])
   
    return dates,news_urls

def get_link_detik(datetime):
    news_urls = []
    dates = []

    for i in range(len(datetime)):
        response = requests.get('https://news.detik.com/indeks/all?date='+datetime[i])
        soup = BeautifulSoup(response.text, 'html.parser')
    
        temp = []
        for ul in soup.findAll('ul', {'id': 'indeks-container'}):
            for article in ul.findAll('article'):
                for a in article.findAll('a'):
                    temp.append(a['href'])
        news_urls.append(temp)
        dates.append(datetime[i])
        print (datetime[i])
    return dates, news_urls

def get_link_metrotvnews(datetime):
    news_urls = []
    dates = []
    
    for i in range(len(datetime)):
        response = requests.get('http://www.metrotvnews.com/index/'+datetime[i])
        soup = BeautifulSoup(response.text, 'html.parser')

        temp = []
        for div in soup.findAll('div', {'class': 'style_06'}):
            for h2 in div.findAll('h2'):
                for a in h2.findAll('a'):
                    temp.append(a['href'])
        news_urls.append(temp)
        dates.append(datetime[i])
        print (datetime[i])
    return dates, news_urls


def get_news_link(start_month, end_month, year, news_site_name):
  
    # TODO : POPULATE datetime
  
    datetime= generate_datetime(start_month, end_month, year, news_site_name)
  
    if news_site_name =='kompas':
        dates, news_urls = get_link_kompas(datetime)
    elif news_site_name == 'tempo':
        dates, news_urls = get_link_tempo(datetime)
    elif news_site_name == 'detik':
        dates, news_urls = get_link_detik(datetime)
    elif news_site_name == 'metrotvnews':
        dates, news_urls = get_link_metrotvnews(datetime)
    df = {'dates': dates, 'links': news_urls}  
    news_link_df = pd.DataFrame(data= df, columns=['dates','links'])
  
    news_link_df.to_csv('data/input/'+news_site_name+'_'+str(year)+'.csv')
    print(news_site_name+'news url saved in /data/input')
    return news_link_df



#%%  


			
			
