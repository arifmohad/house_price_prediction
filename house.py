import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Load the dataset from a CSV file
df = pd.read_csv(r'house_data.csv')

# Select specific columns for the model
columns = ['bedrooms', 'bathrooms', 'sqft_living', 'zipcode', 'price']
df = df[columns]

# Separate features (X) and target variable (y)
X = df.iloc[:, 0:4]  # Features: 'bedrooms', 'bathrooms', 'sqft_living', 'zipcode'
y = df.iloc[:, 4:]   # Target variable: 'price'

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Initialize the Linear Regression model
lr = LinearRegression()

# Train the model using the training data
lr.fit(X_train, y_train)

# Save the trained model to a file using pickle
pickle.dump(lr, open('model.pkl', 'wb'))
