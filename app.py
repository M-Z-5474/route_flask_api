# app.py
from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
with open('safe_route_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return "Safe Route Model is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        features = np.array(data['features']).reshape(1, -1)  # assuming input is a list of features
        prediction = model.predict(features)
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
       app.run(host="0.0.0.0", port=8080, debug=True)

