import re
from bs4 import BeautifulSoup
from urllib.request import urlopen


class CreateSoupMixin(BeautifulSoup):
    def create_soup(self, url):
        html = urlopen(url).read()
        soup = BeautifulSoup(html, features="html.parser")
        return soup


class HtmlToTextMixin(CreateSoupMixin):
    def html_to_text(self):
        soup = self.create_soup()
        for script in soup(["script", "style"]):
            script.extract()
        return soup.get_text()


class ClearTextMixin(HtmlToTextMixin):
    def clear_text(self):
        text = self.html_to_text()
        lines = [line.strip() for line in text.splitlines()]
        clear_text = [phrase.strip() for line in lines for phrase in line.split(" ") if phrase]
        return clear_text


class CountWordsMixin(ClearTextMixin):
    def count_words(self, word):
        clear_text = self.clear_text()
        count_word = 0
        count_all_word = 0
        for line in clear_text:
            for w in re.findall(r"[\w']+", line):
                count_all_word += 1
                if w.lower() == word:
                    count += 1

