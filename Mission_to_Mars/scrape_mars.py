import pymongo
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import requests


def scrape():
    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
        
    # listings = { }

    # URL of page to be scraped
    url = "https://mars.nasa.gov/news"
    # browser.visit(url)

    # Retrieve page with the requests module
    response = requests.get(url)

    #  Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(response.text, 'html.parser')
  
    # Find HTML where title and description reside.
    results = soup.find_all('div', class_='slide')

    # loop over results to get article data (just the first [0:1])
    for result in results[0:1]:

    # OTHERWISE THIS RETURNS JUST ONE TITLE & ONE DESCRIPTION 
        # try:
        
            # scrape the article title & description
            title = result.find('div', class_='content_title' ).text
            description = result.find('div', class_='rollover_description_inner').text
      
        # except AttributeError as e:
        #     # print(e)   

    # # read article title & description into "listings"
    # listings['title'] = results.find('div', class_='content_title' ).text
    # listings['description'] = results.find('div', class_='rollover_description_inner').text


    # # Dictionary to be inserted into MongoDB
    listings = {'title': title,'description': description}

    # # # Insert dictionary into MongoDB as a document
    # listings.insert_one(listings)
  

    browser.quit

    return listings
   

    


# def table():
#     Return df.to_html

# def image()
#     Return of image and name to dict

