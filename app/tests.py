import unittest
import identidock

class TestCase(unittest.TestCase):

    def setUp(self):
        identidock.app.config["TESTING"] = True  # 'TESTNG' -> 'TESTING'
        self.app = identidock.app.test_client()

    def test_get_mainpage(self):
        page = self.app.post("/", data=dict(name="Moby Dock"))
        self.assertEqual(page.status_code, 200)  # 'assert' -> 'self.assertEqual'
        self.assertIn('Hello', str(page.data))  # 'assert ... in' -> 'self.assertIn'
        self.assertIn('Moby Dock', str(page.data))  # 'assert ... in' -> 'self.assertIn'

    def test_html_escaping(self):
        page = self.app.post("/", data=dict(name='"><b>TEST</b><!--')) 
        self.assertNotIn('<b>', str(page.data)) 

if __name__ == '__main__':
    unittest.main()
