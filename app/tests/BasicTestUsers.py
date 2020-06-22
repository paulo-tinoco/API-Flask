import json
import unittest
from app import create_app


class BasicTestUsers(unittest.TestCase):
    
    
    app = create_app()

    def test_get_users(self):
        tester = self.app.test_client(self)
        headers = {
            'email': 'admin@example.com',
            'password': 123456
        }

        res = tester.get('/api/v1/users/', headers=headers, follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn('data',json.loads(res.data))

    def test_post_user(self):
        tester = self.app.test_client(self)
        headers = {
            'email': 'admin@example.com',
            'password': 123456
        }
        data = {
            'name': 'New User',
            'email': 'example@example.com',
            'password': 'example123',
            'role_id': 1
        }

        res = tester.post('/api/v1/users/', headers=headers, json=data, follow_redirects=True)
        self.assertEqual(res.status_code, 201)
        self.assertIn('data',json.loads(res.data))

    def test_update_user(self):
        tester = self.app.test_client(self)
        headers = {
            'email': 'admin@example.com',
            'password': 123456
        }
        data = {
            'status': 0
        }

        id_user = 1

        res = tester.put(f'/api/v1/users/{id_user}', headers=headers, json=data, follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn('data',json.loads(res.data))        

    def test_get_roles(self):
        tester = self.app.test_client(self)
        headers = {
            'email': 'admin@example.com',
            'password': 123456
        }

        res = tester.get('/api/v1/users/roles', headers=headers, follow_redirects=True)
        self.assertEqual(res.status_code, 200)
        self.assertIn('data',json.loads(res.data))

if __name__ == "__main__":
    unittest.main()