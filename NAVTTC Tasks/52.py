
# https://www.datacamp.com/tutorial/understanding-logistic-regression-python

# Understanding Logistic Regression in Python

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    roc_curve,
    roc_auc_score
)

# Load dataset directly from URL
col_names = [
    'pregnant', 'glucose', 'bp', 'skin', 'insulin',
    'bmi', 'pedigree', 'age', 'label'
]

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"

pima = pd.read_csv(url, header=None, names=col_names)

# Display first five rows
print("First five rows:")
print(pima.head())

# Split dataset into features and target variable
feature_cols = [
    'pregnant', 'insulin', 'bmi', 'age',
    'glucose', 'bp', 'pedigree'
]

X = pima[feature_cols]
y = pima['label']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=16,
    stratify=y
)

# Initialize Logistic Regression with feature scaling
logreg = make_pipeline(
    StandardScaler(),
    LogisticRegression(random_state=16, max_iter=1000)
)

# Train the model
logreg.fit(X_train, y_train)

# Predict test data
y_pred = logreg.predict(X_test)

# Confusion Matrix
cnf_matrix = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cnf_matrix)

# Plot Confusion Matrix
class_names = ['Without diabetes', 'With diabetes']

plt.figure(figsize=(7, 5))

sns.heatmap(
    cnf_matrix,
    annot=True,
    cmap='YlGnBu',
    fmt='d',
    xticklabels=class_names,
    yticklabels=class_names
)

plt.title('Confusion Matrix')
plt.xlabel('Predicted Label')
plt.ylabel('Actual Label')
plt.tight_layout()
plt.show()

# Classification Report
target_names = ['Without diabetes', 'With diabetes']

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=target_names,
        zero_division=0
    )
)

# ROC Curve and AUC Score
y_pred_proba = logreg.predict_proba(X_test)[:, 1]

fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
auc = roc_auc_score(y_test, y_pred_proba)

print(f"\nROC-AUC Score: {auc:.4f}")

# Plot ROC Curve
plt.figure(figsize=(7, 5))

plt.plot(
    fpr,
    tpr,
    label=f'Logistic Regression (AUC = {auc:.2f})'
)

plt.plot(
    [0, 1],
    [0, 1],
    linestyle='--',
    label='Random Classifier'
)

plt.title('ROC Curve')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend(loc='lower right')
plt.tight_layout()
plt.show()


'''

https://towardsdatascience.com/five-regression-python-modules-that-every-data-scientist-must-know-a4e03a886853/

# Five Regression Modules in Python
# 1. NumPy polyfit
# 2. SciPy linregress
# 3. Statsmodels OLS
# 4. Scikit-learn LinearRegression
# 5. Seaborn regplot

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import statsmodels.api as sm
from sklearn import linear_model

# Sample dataset: GDP per capita and life satisfaction
x = np.array([
    56755.72171242, 44178.04737774, 40991.80813814,
    8814.00098681, 43585.51198178, 13574.17183072,
    6175.8760297, 17829.69832237, 53254.85637009,
    17522.23018625, 42784.69836164, 36638.18492916,
    41086.72967373, 18167.77372717, 12706.89121489,
    52564.42917946, 61995.42280258, 35776.79516181,
    30230.22630213, 34524.46986093, 13774.60527391,
    14258.22933451, 101376.49657434, 9616.64500569,
    45175.23189338, 38615.99518491, 74355.51585756,
    12578.49547344, 19242.3664711, 16310.988409,
    20881.76692993, 5734.63362915, 25732.01836475,
    51545.48360953, 82081.59716162, 11006.2497364,
    44974.83187718, 56839.38177423
])

y = np.array([
    7.3, 7.1, 6.9, 6.4, 7.4, 6.5, 6.3, 6.7, 7.6,
    5.7, 7.6, 6.5, 7.0, 5.4, 5.6, 7.5, 7.0, 7.2,
    6.0, 5.9, 5.9, 5.9, 6.9, 6.5, 7.4, 7.3, 7.6,
    6.1, 5.4, 6.2, 5.9, 4.7, 6.3, 7.3, 7.5, 5.5,
    6.8, 6.9
])

# --------------------------------------------------
# 1. NumPy polyfit
# --------------------------------------------------
print("\n1. NumPy polyfit")

p = np.poly1d(np.polyfit(x, y, 1))

print("Regression equation:")
print(p)

x_line = np.linspace(np.min(x), np.max(x), 200)

plt.figure(figsize=(8, 5))
plt.scatter(x, y, label="Original data")
plt.plot(x_line, p(x_line), color="red",
         label="Linear regression")
plt.title("NumPy polyfit")
plt.xlabel("GDP per capita (USD)")
plt.ylabel("Life Satisfaction")
plt.legend()
plt.tight_layout()
plt.show()

# --------------------------------------------------
# 2. SciPy linregress
# --------------------------------------------------
print("\n2. SciPy linregress")

regr_results = stats.linregress(x, y)

print(regr_results)

# --------------------------------------------------
# 3. Statsmodels OLS
# --------------------------------------------------
print("\n3. Statsmodels OLS")

X = sm.add_constant(x)
lin_model = sm.OLS(y, X)
ols_results = lin_model.fit()

print("Coefficients:")
print(ols_results.params)

print("\nDetailed regression summary:")
print(ols_results.summary())

# --------------------------------------------------
# 4. Scikit-learn LinearRegression
# --------------------------------------------------
print("\n4. Scikit-learn LinearRegression")

linmodel = linear_model.LinearRegression(
    fit_intercept=True
)

linmodel.fit(x.reshape(-1, 1), y)

slope = linmodel.coef_[0]
intercept = linmodel.intercept_

print("Slope:", slope)
print("Intercept:", intercept)
print("R-squared:", linmodel.score(x.reshape(-1, 1), y))

# Predict life satisfaction for new GDP values
new_x = np.array([20000, 40000, 60000]).reshape(-1, 1)
predictions = linmodel.predict(new_x)

print("\nPredictions:")
for gdp, prediction in zip(new_x.ravel(), predictions):
    print(f"GDP: ${gdp:,.0f} -> Predicted satisfaction: {prediction:.2f}")

# --------------------------------------------------
# 5. Seaborn regplot
# --------------------------------------------------
print("\n5. Seaborn regplot")

fig, ax = plt.subplots(figsize=(10, 6))

sns.regplot(
    x=x,
    y=y,
    ci=95,
    order=1,
    line_kws={
        "label": "Linear regression line",
        "color": "magenta"
    },
    seed=1,
    truncate=False,
    ax=ax
)

ax.set_xlabel("GDP per capita 2015 (USD)")
ax.set_ylabel("Life Satisfaction Value")
ax.set_title("GDP per Capita vs Life Satisfaction")
ax.legend(["Original data", "Linear regression line"])
plt.tight_layout()
plt.show()


'''