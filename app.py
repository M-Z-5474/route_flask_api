from flask import Flask, request, jsonify
import numpy as np
import joblib
import os

app = Flask(__name__)

# Load the model using joblib
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'safe_route_model.pkl')
model = joblib.load(MODEL_PATH)

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
    port = int(os.environ.get('PORT', 8080))
    app.run(host="0.0.0.0", port=port)
