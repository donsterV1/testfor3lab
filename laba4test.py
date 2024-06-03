import unittest
from sait import app

class TestAppMethods(unittest.TestCase):

    def test_index(self):
        with app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)

    def test_post_data(self):
        with app.test_client() as client:
            data = {
                'name': 'User',
                'age': 25,
                'university': 'University',
                'like_university': 'Yes'
            }
            response = client.post('/', data=data)
            self.assertEqual(response.status_code, 200)

    def test_invalid_form(self):
        with app.test_client() as client:
            data = {
                'name': '11234',
                'age': 125,
                'university': 'University',
                'like_university': 'Yes'
            }
            response = client.post('/', data=data)
            self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
