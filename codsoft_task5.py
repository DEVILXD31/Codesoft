# -*- coding: utf-8 -*-
"""CodSoft Task5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RZYDHcG9jEBUqC2QfiwJ7lpYKVhw7s4w
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load the dataset

data = pd.read_csv('creditcard.csv')

# Normalize 'Time' and 'Amount' columns
scaler = StandardScaler()
data[['Time', 'Amount']] = scaler.fit_transform(data[['Time', 'Amount']])

# Separate the majority and minority classes
fraud = data[data['Class'] == 1]
non_fraud = data[data['Class'] == 0]

# Downsample the majority class
non_fraud_downsampled = non_fraud.sample(n=len(fraud), random_state=42)

# Combine the minority class with the downsampled majority class
data_balanced = pd.concat([fraud, non_fraud_downsampled])

# Separate features and target
X_balanced = data_balanced.drop('Class', axis=1)
y_balanced = data_balanced['Class']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_balanced, y_balanced, test_size=0.2, random_state=42)

print("Choose the model to train and evaluate:")
print("1. Logistic Regression")
print("2. Random Forest")
choice = input("Enter the number of your choice: ")

if choice == '1':
    model_type = 'logistic_regression'
    model = LogisticRegression()
elif choice == '2':
    model_type = 'random_forest'
    model = RandomForestClassifier()
else:
    print("Invalid choice. Exiting.")
    exit()

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

report = classification_report(y_test, y_pred)
print(f"Classification report for {model_type.replace('_', ' ').title()}:")
print(report)