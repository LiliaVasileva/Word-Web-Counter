import re
from bs4 import BeautifulSoup
from urllib.request import urlopen


class CreateSoupMixin(BeautifulSoup):
    def create_soup(self, url):
        html = urlopen(url).read()
        soup = BeautifulSoup(html, features="html.parser")
        return soup


class HtmlToTextMixin():
    def html_to_text(self, soup):
        for script in soup(["script", "style"]):
            script.extract()
        return soup.get_text()


class ClearTextMixin():
    def clear_text(self, text):
        lines = [line.strip() for line in text.splitlines()]
        clear_text = [phrase.strip() for line in lines for phrase in line.split(" ") if phrase]
        return clear_text


class CountWordsMixin():
    def count_words(self, word, text):
        count_word = 0
        count_all_word = 0
        for line in text:
            for w in re.findall(r"[\w']+", line):
                count_all_word += 1
                if w.lower() == word:
                    count_word += 1
        return count_word, count_all_word

