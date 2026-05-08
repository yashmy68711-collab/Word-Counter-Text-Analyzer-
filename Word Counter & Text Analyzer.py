print("Word Counter & Text Analyzer")

text = input("Enter your text:\n")

if text.strip() == "":
    print("Text cannot be empty")
    exit()

# Word list
words = text.lower().split()

# Counts
word_count = len(words)
char_count = len(text)
sentence_count = text.count(".") + text.count("!") + text.count("?")

# Most repeated word
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

most_used = max(frequency, key=frequency.get)

print("\n--- Analysis ---")
print("Total Words:", word_count)
print("Total Characters:", char_count)
print("Total Sentences:", sentence_count)
print("Most Repeated Word:", most_used)
print("Repeated Times:", frequency[most_used])