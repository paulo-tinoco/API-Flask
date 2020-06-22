import json
import unittest
from ..app import create_app


class BasicTestProducts(unittest.TestCase):
    
    
    app = create_app()
    
    def test_post_product(self):
        tester = self.app.test_client(self)
        headers = {
            'email': 'admin@example.com',
            'password': 123456
        }
        data = {
            'name': 'Product 07',
            'price': 1.55,
            'quantity': 120
        }

        res = tester.post('/api/v1/products/', headers=headers, json=data, follow_redirects=True)
        self.assertEqual(res.status_code, 201)
        self.assertIn('data',json.loads(res.data))
    
    def test_get_product(self):
        tester = self.app.test_client(self)
        headers = {
            'email': 'admin@example.com',
            'password': 123456
        }

        res = tester.get('/api/v1/products', headers=headers, follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn('data',json.loads(res.data))

    def test_post_categories(self):
        tester = self.app.test_client(self)
        headers = {
            'email': 'admin@example.com',
            'password': 123456
        }
        data = {
            'name': 'Category 5',
            'product_id': 2
        }

        res = tester.post('/api/v1/products/category', headers=headers, json=data, follow_redirects=True)
        self.assertEqual(res.status_code, 201)
        self.assertIn('data',json.loads(res.data))
    
    def test_get_categories(self):
        tester = self.app.test_client(self)
        headers = {
            'email': 'admin@example.com',
            'password': 123456
        }

        res = tester.get('/api/v1/products/category', headers=headers, follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn('data',json.loads(res.data))

if __name__ == "__main__":
    unittest.main()