import re
from bs4 import BeautifulSoup
from urllib.request import urlopen


class CreateSoupMixin(BeautifulSoup):
    """ create_soup() function is creating a BeautifulSoup object which represents the document as a nested data structure. """
    def create_soup(self, url):
        try:
            html = urlopen(url).read()
        except:
            raise Exception('Unable to load the url')
        html = urlopen(url).read()
        soup = BeautifulSoup(html, features="html.parser")
        return soup


class HtmlToTextMixin():
    """
    html_to_text() function accept soup object and clear from the soup object all scripts and styles tags.
    Return text representation of the html.
    """
    def html_to_text(self, soup: object):
        for script in soup(["script", "style"]):
            script.extract()
        return soup.get_text()


class ClearTextMixin():
    """
    clear_text() function accept string and clears all empty spaces and empty lines.
    Returns str: clean text.
    """
    def clear_text(self, text: str):
        lines = [line.strip() for line in text.splitlines()]
        clear_text = [phrase.strip() for line in lines for phrase in line.split(" ") if phrase]
        return clear_text


class CountWordsMixin():
    """
    count_words() function accept word and text, count how many times the word occure in the text, total words in the text
    Returns  int: count_word and count_all_word.
    """
    def count_words(self,word: str, text: str):
        count_word = 0
        count_all_word = 0
        for line in text:
            for w in re.findall(r"[\w']+", line):
                count_all_word += 1
                if w.lower() == word:
                    count_word += 1
        return count_word, count_all_word

