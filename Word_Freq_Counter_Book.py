# Import necessary  libraries
from collections import Counter
import re 

# Load text data
with open('C:\\Users\\mcole\\OneDrive\\Documents\\Books\\The Revolt of Angels.txt', 'r') as file:
    text = file.read()

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