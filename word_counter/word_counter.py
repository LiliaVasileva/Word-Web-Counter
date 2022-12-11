


class WordWebCounter():
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
