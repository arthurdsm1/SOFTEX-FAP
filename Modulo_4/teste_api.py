import unittest
import requests

class TestAPI(unittest.TestCase):
    
    def test_status_code(self):
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        self.assertEqual(response.status_code, 200)
    
    def test_json_response(self):
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        self.assertTrue(response.json())
    
    def test_post_data(self):
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        post = response.json()
        self.assertEqual(post['id'], 1)
        self.assertEqual(post['title'], "sunt aut facere repellat provident occaecati excepturi optio reprehenderit")

if __name__ == '__main__':
    unittest.main()
