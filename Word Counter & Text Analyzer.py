print("Word Counter & Text Analyzer")

text = input("Enter your text:\n")

if text.strip() == "":
    print("Text cannot be empty")
    exit()

words = text.lower().split()

word_count = len(words)
char_count = len(text)
sentence_count = text.count(".") + text.count("!") + text.count("?")

ignore = ["the", "is", "a", "an", "and", "to"]
frequency = {}

for word in words:
    if word in ignore:
        continue
        
    frequency[word] = frequency.get(word, 0) + 1

most_used = max(frequency, key=frequency.get)

longest_word = max(words, key=len)
shortest_word = min(words, key=len)

unique_words = len(set(words))

print("\n--- Analysis ---")
print("Total Words:", word_count)
print("Total Characters:", char_count)
print("Total Sentences:", sentence_count)
print("Unique Words:", unique_words)
print("Longest Word:", longest_word)
print("Shortest Word:", shortest_word)
print("Most Repeated Word:", most_used)
print("Repeated Times:", frequency[most_used])
