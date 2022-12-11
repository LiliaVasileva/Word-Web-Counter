from mixin.mixin import CreateSoupMixin, ClearTextMixin, CountWordsMixin, HtmlToTextMixin


class WordWebCounter(CreateSoupMixin, HtmlToTextMixin, ClearTextMixin, CountWordsMixin):
    """
    On initialization of class WordWebCounter receives word and url.
    The program checks if the word and the url are valid data.
    If they are empty str the program will raise an error with appropriate error massage.
    Please check docs for report() function and __str__ magic method.
    """
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
        """
        report() function create a soup object, then extraxt the text representation of the html,
        clear the text from empty lines and spaces.
        Please check documentation of CreateSoupMixin, HtmlToTextMixin, ClearTextMixin, CountWordsMixin.
        Return message with how many times the given word occures on the url and counts all words.

        """
        soup = self.create_soup(self.__url)
        text = self.html_to_text(soup)
        clean_text = self.clear_text(text)
        count_word, count_all_words = self.count_words(self.__word, clean_text)

        result = f'Occurrences of word <{self.__word}>:' +'\n'
        result += f'- {self.__url} => <{count_word}>' + '\n'
        result += f'- Total words => <{count_all_words}>'

        return result


    def __str__(self):
        """
        Returns message with the main functionality of the class personalized for the current object.

        """
        return f'How many words and how many times the word - "{self.__word}" occur on the "{self.__url}".'



test = WordWebCounter('uniberg', 'https://uniberg.com/en/')
print(test)
print(test.report())
print(test.report.__doc__)
