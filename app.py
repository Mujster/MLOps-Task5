# app.py
from flask import Flask, request, jsonify,render_template
import numpy as np
import joblib 

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return  'ML Model Deployed'
    # return render_template('index.html') 

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    # Convert features to a numpy array
    features = np.array(data['features']).reshape(1, -1)

    # Make prediction
    prediction = model.predict(features)

    # Return prediction
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
