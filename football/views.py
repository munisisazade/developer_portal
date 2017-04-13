from django.shortcuts import render
from django.http import HttpResponse
from football.utilits.tool import LiveWebCrawlerMixin

import dryscrape as Firefox
from bs4 import BeautifulSoup as bs
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

# class ScreapyView(LiveWebCrawlerMixin):
#     template_name = 'html/index.html'
#     crawl_url = 'http://www.livescore.com/'
#     data_class = {'data-type':'container'}
#
#     def get_football_data(self):
#         session = Firefox.Session()
#         session.visit(self.crawl_url)
#         response = session.body()
#         soup = bs(response,'html.parser')
#         result = soup.find('div',self.data_class)
#         return result
#
#     def get(self, request, *args, **kwargs):
#         find = self.get_football_data()
#         return HttpResponse(find)