from flask import Flask, request, jsonify
import numpy as np
import joblib
import os

app = Flask(__name__)

# Load the model using joblib
model = joblib.load('safe_route_model.pkl')

@app.route('/')
def home():
    return "✅ Safe Route Model API is live!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        features = np.array(data['features']).reshape(1, -1)
        prediction = model.predict(features)
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)}), 400



if __name__ == '__main__':
       app.run(host="0.0.0.0", port=8080, debug=True)
