import re
import unicodedata

def normalize_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Normalize Unicode characters
    text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')
    
    return text

# Example usage
input_text = "Hello, World!  This is some sample text... With ÜNIÇöde characters."
normalized_text = normalize_text(input_text)
print(f"Original text: {input_text}")
print(f"Normalized text: {normalized_text}")