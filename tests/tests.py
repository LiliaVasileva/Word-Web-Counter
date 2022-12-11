import unittest
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
from word_counter.word_counter import WordWebCounter
from mixin.mixin import CreateSoupMixin, ClearTextMixin, CountWordsMixin, HtmlToTextMixin

class TestWordWebCounter(unittest.TestCase):
    def setUp(self):
        self.word_counter = WordWebCounter('uniberg', 'https://uniberg.com/en/')

    def test_if_when_valid_data_is_given_creates_object(self):
        assert isinstance(self.word_counter,WordWebCounter)

    def test_if_when_no_word_given_raise_error(self):
        self.assertRaises(ValueError,WordWebCounter, "", "https://uniberg.com/en/" )

    def test_if_when_no_url_given_raise_error(self):
        self.assertRaises(ValueError,WordWebCounter, "uniberg", "" )

    def test_if_when_printing_object_return_correct_message(self):
        message = 'How many words and how many times the word - "uniberg" occur on the "https://uniberg.com/en/".'
        self.assertEqual(self.word_counter.__str__(), message)

    def test_if_when_report_is_called_returns_correct_message(self):
        result = 'Occurrences of word <uniberg>:' +'\n'
        result += '- https://uniberg.com/en/ => <8>' + '\n'
        result += '- Total words => <957>'
        self.assertEqual(self.word_counter.report(), result)


class TestCreateSoupMixin(unittest.TestCase):
    def setUp(self):
        self.url = 'https://uniberg.com/en/'

    def test_if_creates_soup_object(self):
        html = urlopen(self.url).read()
        soup = BeautifulSoup(html, features="html.parser")
        assert isinstance(soup, BeautifulSoup)


class TestHtmlToTextMixin(unittest.TestCase):
    def setUp(self):
        self.url = 'https://uniberg.com/en/'
        self.word = 'uniber'

    def test_if_valid_text_data_is_returned_from_html_to_text_function(self):
        web_counter = WordWebCounter(self.word, self.url)
        soup = web_counter.create_soup(self.url)
        text = web_counter.html_to_text(soup)

        url = 'https://uniberg.com/en/'
        html = urlopen(url).read()
        test_soup = BeautifulSoup(html, features="html.parser")

        for script in test_soup(["script", "style"]):
            script.extract()

        test_soup_text = test_soup.get_text()

        self.assertEqual(text, test_soup_text)


class TestClearTextMixin(unittest.TestCase):
    def setUp(self):
        self.url = 'https://uniberg.com/en/'
        self.word = 'uniber'

    def test_if_clean_text_data_is_returned_from_clear_text_function(self):
        web_counter = WordWebCounter(self.word, self.url)
        soup = web_counter.create_soup(self.url)
        text = web_counter.html_to_text(soup)
        clear_text = web_counter.clear_text(text)

        url = 'https://uniberg.com/en/'
        html = urlopen(url).read()
        test_soup = BeautifulSoup(html, features="html.parser")

        for script in test_soup(["script", "style"]):
            script.extract()

        test_soup_text = test_soup.get_text()
        lines = [line.strip() for line in test_soup_text.splitlines()]
        clear_text_test = [phrase.strip() for line in lines for phrase in line.split(" ") if phrase]

        self.assertEqual(clear_text, clear_text_test)


class TestCountWordsMixin(unittest.TestCase):
    def setUp(self):
        self.url = 'https://uniberg.com/en/'
        self.word = 'uniberg'

    def test_if_valid_count_of_given_word_and_valid_count_of_all_words_is_given(self):
        web_counter = WordWebCounter(self.word, self.url)
        soup = web_counter.create_soup(self.url)
        text = web_counter.html_to_text(soup)
        clear_text = web_counter.clear_text(text)
        count_word, count_all_word = web_counter.count_words(self.word, clear_text)

        url = 'https://uniberg.com/en/'
        html = urlopen(url).read()
        test_soup = BeautifulSoup(html, features="html.parser")

        for script in test_soup(["script", "style"]):
            script.extract()

        test_soup_text = test_soup.get_text()
        lines = [line.strip() for line in test_soup_text.splitlines()]
        clear_text_test = [phrase.strip() for line in lines for phrase in line.split(" ") if phrase]
        count_word_test = 0
        count_all_word_test = 0
        for line in clear_text_test:
            for w in re.findall(r"[\w']+", line):
                count_all_word_test += 1
                if w.lower() == "uniberg":
                    count_word_test += 1

        self.assertEqual(count_word, count_word_test)
        self.assertEqual(count_all_word, count_all_word_test)



if __name__ == '__main__':
    unittest.main()