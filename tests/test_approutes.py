from main.app import app

import unittest


class DukaTestCase(unittest.TestCase):
    """Basic test case for access to index page."""

    def test_index(self):
        """Test access to landing page."""
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')


if __name__ == '__main__':
    unittest.main()
