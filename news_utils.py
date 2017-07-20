#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 09:57:47 2017

@author: dwi
"""
import scraper
date_separator = {
        'kompas':'-',
        'tempo':'/'
        }

get_article = {
        'kompas':scraper.get_news_kompas,
        'tempo':scraper.get_news_tempo
        }
