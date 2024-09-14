import unittest
from app import app
import json

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_predict(self):
        response = self.client.post('/predict', 
            data=json.dumps({
                'BEDROOMS': 3,
                'BATHROOMS': 2,
                'GARAGE': 1,
                'LAND_AREA': 500,
                'FLOOR_AREA': 150,
                'BUILD_YEAR': 2000,
                'CBD_DIST': 10
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('price', json.loads(response.data))

if __name__ == '__main__':
    unittest.main()
