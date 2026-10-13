from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training data
documents = [
    "just plain boring",
    "entirely predictable and lacks energy",
    "no surprises and very few laughs",
    "very powerful",
    "the most fun film of the summer"
]

# Labels: - = Negative, + = Positive
labels = ["-", "-", "-", "+", "+"]

# Convert text into Bag of Words
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)

# Train Naive Bayes model
model = MultinomialNB()
model.fit(X, labels)

# Test document
test = ["predictable with no fun"]

# Convert test document into Bag of Words
X_test = vectorizer.transform(test)

# Prediction
prediction = model.predict(X_test)

print("Prediction:", prediction[0])