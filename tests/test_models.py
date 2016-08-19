from main.models import User
import unittest


class DukaModelsTest(unittest.TestCase):
    """Test the creation and manipulation of models."""

    def setUp(self):
        """Add initial test configurations."""
        pass

    def tearDown(self):
        """DB cleanup after tests."""
        User.objects.all().delete()

    def test_user_model(self):
        """Test correct creation of new users."""
        new_user = User(username='me', password='meow')
        self.assertIsInstance(new_user, User)
        self.assertEqual(len(User.objects.all()), 1)
