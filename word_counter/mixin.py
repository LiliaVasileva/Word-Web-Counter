import re
from bs4 import BeautifulSoup
from urllib.request import urlopen


class CreateSoupMixin(BeautifulSoup):
    def create_soup(self, url):
        html = urlopen(url).read()
        soup = BeautifulSoup(html, features="html.parser")
        return soup









