
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix

# 1. Load Dataset
col_names = [
    'pregnant', 'glucose', 'bp', 'skin',
    'insulin', 'bmi', 'pedigree', 'age', 'label'
]

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"

pima = pd.read_csv(url, header=None, names=col_names)

print("First five rows:")
print(pima.head())
print("\nDataset shape:", pima.shape)

# 2. Feature Selection
feature_cols = [
    'pregnant', 'insulin', 'bmi', 'age',
    'glucose', 'bp', 'pedigree'
]

X = pima[feature_cols]
y = pima['label']

# 3. Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=1
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

# 4. Build Default Decision Tree
clf = DecisionTreeClassifier(random_state=1)

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print("\nDefault Decision Tree")
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=['Without diabetes', 'With diabetes'],
    zero_division=0
))

cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

# 5. Visualize Default Decision Tree
plt.figure(figsize=(20, 10))

plot_tree(
    clf,
    feature_names=feature_cols,
    class_names=['Without diabetes', 'With diabetes'],
    filled=True,
    rounded=True,
    fontsize=8
)

plt.title("Default Decision Tree")
plt.tight_layout()
plt.show()

# 6. Optimize Decision Tree
clf = DecisionTreeClassifier(
    criterion='entropy',
    max_depth=3,
    random_state=1
)

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print("\nOptimized Decision Tree")
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=['Without diabetes', 'With diabetes'],
    zero_division=0
))

cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

# 7. Visualize Optimized Decision Tree
plt.figure(figsize=(16, 8))

plot_tree(
    clf,
    feature_names=feature_cols,
    class_names=['Without diabetes', 'With diabetes'],
    filled=True,
    rounded=True,
    fontsize=10
)

plt.title("Optimized Decision Tree (max_depth=3)")
plt.tight_layout()
plt.show()

# 8. Create a Decision Stump
stump = DecisionTreeClassifier(
    max_depth=1,
    random_state=1
)

stump.fit(X_train, y_train)
stump_pred = stump.predict(X_test)

print("\nDecision Stump")
print("Accuracy:", metrics.accuracy_score(y_test, stump_pred))

# Visualize Decision Stump
plt.figure(figsize=(10, 5))

plot_tree(
    stump,
    feature_names=feature_cols,
    class_names=['Without diabetes', 'With diabetes'],
    filled=True,
    rounded=True,
    fontsize=10
)

plt.title("Decision Stump (max_depth=1)")
plt.tight_layout()
plt.show()
