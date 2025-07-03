# 🛣️ Safe Route Prediction API - Flask

This is a Flask-based REST API developed on behalf of a **client** to predict safe routes using a pre-trained machine learning model. The model returns predictions based on feature inputs provided in JSON format.

## 🤝 About the Project

This project was implemented by **Muhammad Zain Mushtaq** for a client as part of a data-driven solution to assist in route safety classification. The core functionality includes receiving structured input data, processing it through a trained model, and returning a prediction via an API endpoint.


## 🚀 Features

- 🔌 Simple REST API built with Flask
- 📦 Accepts JSON input with structured feature arrays
- 🤖 Loads and uses a pre-trained model (`safe_route_model.pkl`)
- 🔁 Returns classification results via `/predict` endpoint
- 🌐 Supports deployment using Gunicorn


## 🧠 Tech Stack

- Python 3.8+
- Flask
- Scikit-learn (for model training)
- joblib (for model serialization)


## 📁 Repository Structure
├── app.py # Main Flask application

├── safe_route_model.pkl # Pre-trained ML model

├── requirements.txt # Python dependencies

├── README.md

## 👨‍💻 AI Developer
This API was developed by Muhammad Zain Mushtaq for a client project.

📧 Email: m.zainmushtaq74@gmail.com

🔗 LinkedIn: https://www.linkedin.com/in/muhammad-zain-m-a75163358/
