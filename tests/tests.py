import unittest
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





if __name__ == '__main__':
    unittest.main()