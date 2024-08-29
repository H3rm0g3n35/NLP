# Import necessary  libraries
from collections import Counter
import re 

# Load text data
text = "This is some words that I'm just using to test out this awesome noew script I'm writing."

# Preprocess the text
# Convert to lowercase
text = text.lower()

# Remove punctuation and special characters
text = re.sub(r'[^\w\s]', '', text)

# Tokenize the text into words
words = text.split()

# Count the frequency of each word
word_count = Counter(words)

# Display the word frequencies
for word, count in word_count.most_common():
    print(f"{word}: {count}")