from unittest import TestCase

from wordfrequency.workdaywordfrequencyoutput import WorkdayWordFrequencyOutput

class TestWordFrequencyOutput(TestCase):

    def test_format(self):

        input = [[("Adrian", 6)],[("Hynes", 5),("Python",5)],[("Kubernetes", 4)]]
        workfrequencyoutput = WorkdayWordFrequencyOutput(input, 3)
        expected = "Top 3 words:\n- 6 Adrian \n- 5 Hynes, Python \n- 4 Kubernetes \n"
        output = workfrequencyoutput.format()

        self.assertEqual(output, expected)

