# %%%% Preliminaries and library loading
import datetime
import os
import pandas as pd
import re
import shelve
import time
import datetime
import requests

# libraries to crawl websites
from bs4 import BeautifulSoup
from selenium import webdriver
#from pynput.mouse import Button, Controller


pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 5)
pd.set_option('display.width',800)


driver = webdriver.Chrome('C:/Users/jerri/Downloads/chromedriver87.exe')


# %%% 


#Creating the list of links.
links_to_scrape = ['https://www.imdb.com/list/ls056549735/']
one_link = links_to_scrape[0]
driver.get(one_link)
link = ['https://www.imdb.com/list/ls056549735/',
            'https://www.imdb.com/list/ls056549735/?sort=list_order,asc&st_dt=&mode=detail&page=2',
            'https://www.imdb.com/list/ls056549735/?sort=list_order,asc&st_dt=&mode=detail&page=3',
            'https://www.imdb.com/list/ls056549735/?sort=list_order,asc&st_dt=&mode=detail&page=4',
            'https://www.imdb.com/list/ls056549735/?sort=list_order,asc&st_dt=&mode=detail&page=5',
            'https://www.imdb.com/list/ls056549735/?sort=list_order,asc&st_dt=&mode=detail&page=6',
            'https://www.imdb.com/list/ls056549735/?sort=list_order,asc&st_dt=&mode=detail&page=7',
            'https://www.imdb.com/list/ls056549735/?sort=list_order,asc&st_dt=&mode=detail&page=8',
            'https://www.imdb.com/list/ls056549735/?sort=list_order,asc&st_dt=&mode=detail&page=9',
            'https://www.imdb.com/list/ls056549735/?sort=list_order,asc&st_dt=&mode=detail&page=10',
            'https://www.imdb.com/list/ls056549735/?sort=list_order,asc&st_dt=&mode=detail&page=11']
            


# %%% 
# Finding all the reviews in the website and bringing them to python
total_movie_review = []
for i in link:
    # i = 'https://www.imdb.com/list/ls056549735/'
    reviews           = requests.get(i).content

    soup                         = BeautifulSoup(reviews,'lxml')
            
    movie_list = soup.find_all('div',{'class':'lister-item mode-detail'})
    r                 = 0
    for r in range(len(movie_list)):
        one_review                   = {}
        one_review['scrapping_date'] = datetime.datetime.now()
        one_review['url']            = driver.current_url
    
    # get the order
        movie_order = movie_list[r].find_all('span')
        if movie_order == []:
            one_review_order = ''
        else:
            one_review_order = movie_order[0].text
        one_review['movie_order']= one_review_order
        
    # get the movie name
        movie_name = movie_list[r].find_all('a')
        if movie_name == []:
            one_review_name = ''
        else:
            one_review_name = movie_name[1].text
        one_review['movie_name']= one_review_name
        
     
     # get the year 
        movie_year = movie_list[r].find_all('span')
        if movie_year == []:
            one_review_year = ''
        else:
            one_review_year = movie_year[1].text
        one_review['movie_year']= one_review_year
        
      # get the classifier 
        movie_class = movie_list[r].find_all('span')
        if movie_class == []:
            one_review_class = ''
        else:
            one_review_class = movie_class[2].text
        one_review['movie_classifier']= one_review_class     
        
    # get the duration 
        movie_dur = movie_list[r].find_all('span')
        if movie_dur == []:
            one_review_dur = ''
        else:
            one_review_dur = movie_dur[4].text
        one_review['movie_duration']= one_review_dur
        
     # get the review 
        movie_review = movie_list[r].find_all('p')
        if movie_review == []:
            one_review_review = ''
        else:
            one_review_review = movie_review[1].text
        one_review['movie_review']= one_review_review
        
    # get genre   
        movie_genre = movie_list[r].find_all('span')
        try:
            one_review_genre = movie_genre[6].text 
        except IndexError:
            one_review_genre = ''
        one_review['movie_genre']= one_review_genre
    
     # get the star
        movie_star = movie_list[r].find_all('span')
        try:
            one_review_stars = movie_star[8].text 
        except IndexError:
            one_review_stars = ''
        one_review['movie_star']= one_review_stars    
  
    # get the director
        movie_director = movie_list[r].find_all('a')
        try:
            one_review_director = movie_director[13].text 
        except IndexError:
            one_review_director = ''
        one_review['movie_director']= one_review_director         
  
    # get the votes
        movie_votes = movie_list[r].find_all('span')
        try:
            one_review_votes = movie_votes[59].text 
        except IndexError:
            one_review_votes = ''
        one_review['movie_votes']= one_review_votes 

    # get the gross
        movie_gross = movie_list[r].find_all('span')
        try:
            one_review_gross = movie_gross[62].text 
        except IndexError:
            one_review_gross = ''
        one_review['movie_gross']= one_review_gross
        
        
        total_movie_review.append(one_review)
# %%%% More cleaning
a = pd.DataFrame.from_dict(total_movie_review)
# BeautifulSoup(a.review_raw.iloc[0]).text
a.to_excel('movies.xlsx')





