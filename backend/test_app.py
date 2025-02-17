import unittest
from app import app

class FlaskAPITestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def test_hello(self):
        """Test the root endpoint returns correct message"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Hello from Flask!", response.json["message"])

    def test_heartbeat(self):
        """Test the heartbeat endpoint"""
        response = self.client.get("/heartbeat")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "running", "service": "flask-backend"})

if __name__ == "__main__":
    unittest.main()
