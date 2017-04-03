from django.shortcuts import render

# Create your views here.


"""
    Scraping with JS support:

>>> import dryscrape
>>> from bs4 import BeautifulSoup
>>> session = dryscrape.Session()
>>> session.visit(<MY_GRAB_URL>)
>>> response = session.body()
>>> soup = BeautifulSoup(response)
>>> soup.find(id="intro-text")
<p id="intro-text">Yay! Supports javascript</p>

    Find by all attribute name element:

    myfilter = soup.find_all("<DOM_ELEMENT_NAME>", { "<ATTRIBUTE_NAME>" : "<ATTRIBUTE_VALUE>" })



"""