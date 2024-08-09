# house_price_prediction

In this project, I developed the predictive power of a model trained on house price data. It deploys with flask API and uses Linear Regression to predict the price value. Deploy Machine Learning Model Using Flask to take a model from python code.


# Installation

To run the web app on your local computer, install the required libraries. These packages are include in the requirement.txt file. This project used Python 3.11.1 and Flask 3.0.3. Run the following command in the terminal to install the required packages.

```
pip install -r requirement.txt
```
# Zip Code Location API

http://api.zippopotam.us

The Zippopotam API provides information about the location associated with a given ZIP code in the United States. It returns details such as the city and state for the ZIP code.

# Getting Started

To run code on your computer, following command in terminal
```
python app.py
```
# Running on localhost

Running on http://127.0.0.1:5000


# Data Set Constraints

- **Maximum Bedrooms**: 5
- **Maximum Bathrooms**: 4
- **Maximum Square Feet**: 4500
- **Zipcodes**: Must be from Washington, USA

**Note:** The dataset used in this application is minimal, meaning it only includes a limited range of values. For practical purposes, the application is configured to handle properties with up to 5 bedrooms, 4 bathrooms, and 4500 square feet. Additionally, ZIP codes must be from Washington, USA, to ensure the data remains relevant to the application's intended use case.


# How It Works

The application is designed to predict house prices based on user inputs, such as the number of bedrooms, bathrooms, and square feet. Here’s a step-by-step overview of how it operates:

1. **User Input**: 
   - Users provide details about the house they are interested in, including the number of bedrooms (up to 5), bathrooms (up to 4), and the size in square feet (up to 4500). They also enter a ZIP code for the location of the property.

2. **Data Constraints**: 
   - The application is configured to work with a minimal dataset, meaning it only handles properties within the specified limits. This ensures that predictions are made within a manageable and relevant range.

3. **ZIP Code Validation**:
   - The provided ZIP code must be from Washington, USA. The application uses the Zippopotam API to validate and retrieve location information associated with the ZIP code. The API endpoint used is:
     ```
     http://api.zippopotam.us/us/{zipcode}
     ```
   - This API provides details such as city and state based on the ZIP code, which helps in ensuring that the ZIP code is valid and falls within the specified region.

4. **Prediction**:
   - Based on the validated inputs, the application uses a pre-trained machine learning model to predict the house price. The model takes into account the provided features and returns a price estimate.

5. **Output**:
   - The predicted house price is then displayed to the user.

By adhering to these constraints and using the Zippopotam API for location validation, the application ensures that predictions are accurate and relevant to the specified dataset.
