#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 13:21:50 2017

@author: dwi
"""
import populate_news_link
import prepare_news_data

news_site_names = ['kompas','detik','metrotvnews']
years = [2016, 2015]
for year in years:
    for name in news_site_names:
        populate_news_link.get_news_link(1,1,year,name)
        prepare_news_data.prepare(name, year)
    

#%%
# Merge Data in Intermediete Folder
import os 
import pandas as pd

merged = []

for file in os.listdir('data/intermediate/'):
    curr_file = pd.read_csv('data/intermediate/'+file)
    merged.append(curr_file)
    
merged = pd.concat(merged)
merged.to_csv('all_site_'+'_'+str(years[0])+'-'+str(years[-1])+'.csv')