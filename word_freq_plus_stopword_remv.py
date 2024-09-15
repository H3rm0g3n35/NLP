# Import libraries
from collections import Counter
import re
import string

# Prompt for user input.
user_input = input("Please enter text to receive word count frequencies: ")

# Convert to lowercase.
user_input = user_input.lower()

# Remove punctuation and special characters
user_input = re.sub(r'[^\w\s]', '', user_input)

# Tokenize the text into words.
words = user_input.split()

# Count the frequency of each word.
word_count = Counter(words)

# Define a list of stop words.
stop_words = set(['a', 'an', 'and', 'the', 'in', 'on', 'at,' 'to', 'for', 'of', 'is', 'are'])

# Remove stop words
filtered_words = [word for word in words if word not in stop_words]

# Join the words back into a string.
" ".join(filtered_words) 

# Print user input filtered for stop words.
user_input = filtered_words 

print("\n")
print("TEXT AFTER STOP WORDS REMOVED: ")
print(user_input)

# Return word frequencies.
print("\n")
print("WORD FREQUENCY DISTRIBUTION: ")
for word, count in word_count.most_common():
    print(f"{word}: {count}")
    
print("\n")