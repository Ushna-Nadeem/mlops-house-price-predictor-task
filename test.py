import unittest
import requests


class TestHousePricePredictionAPI(unittest.TestCase):

    BASE_URL = "http://localhost:5000/predict"

    def setUp(self):
        # Test data
        self.valid_payload = {
            "BEDROOMS": 3,
            "BATHROOMS": 2,
            "GARAGE": 1,
            "LAND_AREA": 500,
            "FLOOR_AREA": 200,
            "BUILD_YEAR": 2000,
            "CBD_DIST": 10,
        }
        self.invalid_payload = {
            "BEDROOMS": 3,
            "GARAGE": 1,
            "LAND_AREA": 500,
            "FLOOR_AREA": 200,
            "BUILD_YEAR": 2000,
            "CBD_DIST": 10,
        }  # Missing BATHROOMS key

    def test_valid_prediction(self):
        response = requests.post(self.BASE_URL, json=self.valid_payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("price", data)
        print(f"Predicted Price: {data['price']}")

    def test_invalid_prediction(self):
        response = requests.post(self.BASE_URL, json=self.invalid_payload)
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertIn("error", data)
        print(f"Error: {data['error']}")


if __name__ == "__main__":
    unittest.main()
