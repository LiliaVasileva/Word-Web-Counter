from mixin import CreateSoupMixin, ClearTextMixin, CountWordsMixin, HtmlToTextMixin


class WordWebCounter(CreateSoupMixin, HtmlToTextMixin, ClearTextMixin, CountWordsMixin):
    def __init__(self, word, url):
        self.word = word
        self.url = url

    @property
    def word(self):
        return self.word

    @word.setter
    def word(self, value):
        if value == "":
            raise ValueError("Word cannot be a empty value")
        self.__word = value

    @property
    def url(self):
        return self.url

    @url.setter
    def url(self, value):
        if value == "":
            raise ValueError("URL cannot be a empty value")
        self.__url = value


    def report(self):
        soup = self.create_soup(self.__url)
        text = self.html_to_text(soup)
        clean_text = self.clear_text(text)
        count_word, count_all_words = self.count_words(self.__word, clean_text)

        result = f'Occurrences of word <{self.__word}>:' +'\n'
        result += f'- {self.__url} => <{count_word}>' + '\n'
        result += f'- Total words => <{count_all_words}>'

        return result


    def __str__(self):
        return f'How many words and how many times the word - "{self.__word}" occur on the "{self.__url}".'



test = WordWebCounter('uniberg', 'https://uniberg.com/en/')
print(test)
print(test.report())