import string

def exclude_stop_words(lexical_content, stop_words):
    # Convert the text to lowercase
    lexical_content = lexical_content.lower()
    
    # Remove punctuation
    lexical_content = lexical_content.translate(str.maketrans("", "", string.punctuation))
    
    # Split the text into words
    words = lexical_content.split()
    
    # Remove stop words
    filtered_words = [word for word in words if word not in stop_words]
    
    # Join the words back into a string
    return " ".join(filtered_words)

# Define a list of stop words
stop_words = set(['a', 'an', 'and', 'the', 'in', 'on', 'at', 'to', 'for', 'of', 'is', 'are'])

# Example usage
user_input = input("Please enter text to remove stop words. ")
result = exclude_stop_words(user_input, stop_words)

print("Original text:")
print(user_input)
print("\nText after removing stop words:")
print(result)


