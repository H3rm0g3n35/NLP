import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pickle
import re

class TextClassifier:
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.model = MultinomialNB()

    def preprocess_text(self, text):
        # Convert to lowercase and remove punctuation
        text = re.sub(r'[^\w\s]', '', text.lower())
        return text

    def train(self, X, y):
        # Preprocess the text data
        X = [self.preprocess_text(text) for text in X]

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Vectorize the text data
        X_train_vectorized = self.vectorizer.fit_transform(X_train)
        X_test_vectorized = self.vectorizer.transform(X_test)

        # Train the model
        self.model.fit(X_train_vectorized, y_train)

        # Evaluate the model
        y_pred = self.model.predict(X_test_vectorized)
        print(classification_report(y_test, y_pred))

    def predict(self, text):
        text = self.preprocess_text(text)
        text_vectorized = self.vectorizer.transform([text])
        return self.model.predict(text_vectorized)[0]

    def save_model(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump((self.vectorizer, self.model), f)

    def load_model(self, filename):
        with open(filename, 'rb') as f:
            self.vectorizer, self.model = pickle.load(f)

def main():
    # Sample data (you would typically load this from a file)
    X = [
        "I love this movie", "The acting was terrible", "Great special effects",
        "Poor plot and dialogues", "Amazing performance by the lead actor"
    ]
    y = ["positive", "negative", "positive", "negative", "positive"]

    classifier = TextClassifier()

    while True:
        print("\nText Classifier Menu:")
        print("1. Train model")
        print("2. Make prediction")
        print("3. Save model")
        print("4. Load model")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            classifier.train(X, y)
        elif choice == '2':
            text = input("Enter text to classify: ")
            prediction = classifier.predict(text)
            print(f"Prediction: {prediction}")
        elif choice == '3':
            filename = input("Enter filename to save model: ")
            classifier.save_model(filename)
            print(f"Model saved to {filename}")
        elif choice == '4':
            filename = input("Enter filename to load model: ")
            classifier.load_model(filename)
            print(f"Model loaded from {filename}")
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()