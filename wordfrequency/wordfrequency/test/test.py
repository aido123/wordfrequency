from wordfrequency.wordfrequency import count_words,top_words,format
from collections import Counter

expected = [[("Adrian", 6)],[("Hynes", 5)],[("Kubernetes", 4)]]
#input = Counter(["Adrian", "Hynes", "Kubernetes", "Adrian", "Hynes", "Kubernetes", "Adrian", "Hynes", "Kubernetes", "Adrian", "Hynes", "Kubernetes", "Adrian", "Hynes", "Adrian", "Other", "Test"]).items()

input = ([('Adrian', 6), ('Hynes', 5), ('Kubernetes', 4), ('Other', 1), ('Test', 1)])
print(input)
output = top_words(input,3)
print(output)
#      self.assertEqual(output, expected)


