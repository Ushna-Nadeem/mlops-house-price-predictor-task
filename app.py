from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)  # Allow CORS

# Load the model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    try:
        # Extract features from the input data
        features = np.array(
            [
                data["BEDROOMS"],
                data["BATHROOMS"],
                data["GARAGE"],
                data["LAND_AREA"],
                data["FLOOR_AREA"],
                data["BUILD_YEAR"],
                data["CBD_DIST"],
            ]
        ).reshape(1, -1)

        # Make prediction
        prediction = model.predict(features)
        return jsonify({"price": prediction[0]})
    except KeyError:
        return jsonify({"error": "Invalid input"}), 400


if __name__ == "__main__":
    app.run(debug=True)
