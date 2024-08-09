import requests
from flask import Flask, render_template, request
import numpy as np
import pickle

# Initialize the Flask application
app = Flask(__name__)

# Load the pre-trained machine learning model from a pickle file
model = pickle.load(open('model.pkl', 'rb'))

def get_location_from_zipcode(zipcode):
    """
    Given a ZIP code, this function retrieves the location name using the Zippopotam API.

    """
    try:
        # Define the URL for the Zippopotam API request
        url = f"http://api.zippopotam.us/us/{zipcode}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()

        # Check if the response contains 'places' and if it has data
        if 'places' in data and len(data['places']) > 0:
            place = data['places'][0]
            location_name = f"{place.get('place name', '')}, {place.get('state abbreviation', '')}, {place.get('state', '')}, {place.get('country', '')}"
            if location_name.strip():
                print(f"Location: {location_name.strip()}")
                return location_name.strip()
        else:
            print('No data found for the given ZIP code.')
            return None
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

@app.route('/')
def index():
    """
    Renders the index page of the application.

    """
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """
    Handles the prediction request. Retrieves form data, performs a prediction using the ML model,
    and renders the result on the index page.

    Returns:
        str: The rendered HTML template for the index page with prediction result and location name.
    """
    # Get form data from the request
    val1 = request.form['bedrooms']  # Number of bedrooms
    val2 = request.form['bathrooms']  # Number of bathrooms
    val3 = request.form['sqft_living']  # Size of the living area in square feet
    val4 = request.form['zipcode']  # ZIP code for location

    # Get location name from the ZIP code
    location_name = get_location_from_zipcode(val4)

    # Prepare data for prediction
    arr = np.array([val1, val2, val3, float(val4)])  # Convert form data to numpy array
    arr = arr.astype(np.float64)  # Ensure correct data type
    pred = model.predict([arr])  # Perform prediction using the loaded model

    # Render the index page with prediction result and location name
    return render_template('index.html', data=int(pred), location_name=location_name)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
