# Import necessary  libraries
from collections import Counter
import re 

# Load text data
user_input = input("Please enter text for a word count list: ")

# Preprocess the text
# Convert to lowercase
user_input = user_input.lower()

# Remove punctuation and special characters
user_input = re.sub(r'[^\w\s]', '', user_input)

# Tokenize the text into words
words = user_input.split()

# Count the frequency of each word
word_count = Counter(words)

# Display the word frequencies
for word, count in word_count.most_common():
    print(f"{word}: {count}")
