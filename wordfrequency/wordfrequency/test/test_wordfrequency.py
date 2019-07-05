from wordfrequency.wordfrequency import count_words,top_words,format
from unittest import TestCase

class TestWordFrequency(TestCase):

    def test_count_words_happy_path(self):
        text = "adrian hynes this8 the will 799oil anothertest howya, yipee. <test>"
        output = count_words(text)
        self.assertEqual(len(output), 7)

    def test_count_words_input_none_error(self):
        text = None
        with self.assertRaises(TypeError) as err:
            output = count_words(text)
        self.assertRaises(TypeError)

    def test_top_words(self):
      expected = [[("Adrian", 6)],[("Hynes", 5)],[("Kubernetes", 4)]]
      input = ([('Adrian', 6), ('Hynes', 5), ('Kubernetes', 4), ('Other', 1), ('Test', 1)])

      output = top_words(input,3)
      self.assertEqual(output, expected)

    def test_top_words_empty(self):
      expected = []
      input = ([])

      output = top_words(input,50)
      self.assertEqual(output, expected)

    def test_format(self):

        expected = "Top 3 words:\n- 6 Adrian \n- 5 Hynes, Python \n- 4 Kubernetes \n"
        input = [[("Adrian", 6)],[("Hynes", 5),("Python",5)],[("Kubernetes", 4)]]
        output = format(input,3)

        self.assertEqual(output, expected)
