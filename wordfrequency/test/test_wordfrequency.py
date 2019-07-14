from unittest import TestCase

from wordfrequency.workdaywordfrequency import WorkdayWordFrequency

class TestWordFrequency(TestCase):

    def test_count_words_happy_path(self):
        text = "adrian hynes this8 the will 799oil anothertest howya, yipee. <test>"
        workfrequency = WorkdayWordFrequency(text, 2)
        output = workfrequency.count_words()
        self.assertEqual(len(output), 7)

    def test_count_words_input_none_error(self):
        text = None
        with self.assertRaises(TypeError) as err:
            workfrequency = WorkdayWordFrequency(text, 2)
            output = workfrequency.count_words()
        self.assertRaises(TypeError)

    def test_top_words(self):
      expected = [[("Adrian", 6)],[("Hynes", 5)],[("Kubernetes", 4)]]
      input = "Adrian Adrian Adrian Adrian Adrian Adrian Hynes Hynes Hynes Hynes Hynes Kubernetes Kubernetes Kubernetes Kubernetes Other Test"

      workfrequency = WorkdayWordFrequency(input, 3)
      output = workfrequency.top_words()
      self.assertEqual(output, expected)

    def test_top_words_empty(self):
      expected = []
      input = ""

      workfrequency = WorkdayWordFrequency(input, 50)
      output = workfrequency.top_words()
      self.assertEqual(output, expected)
