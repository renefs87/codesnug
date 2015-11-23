from django.core.urlresolvers import reverse
from django.test import TestCase, Client
# Create your tests here.
from codesnug_2.users.models import CodesnugUser


class UserViewsTestCase(TestCase):
    client = None

    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_home(self):
        #Simple get
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


# Create your tests here.
class CodesnugUserModelTestCase(TestCase):
    def test_add_user(self):
        CodesnugUser.objects.create_user('user1', 'user1@test.com', '1111')
        CodesnugUser.objects.create_user('user2', 'user2@test.com', '1111')

        self.assertEqual(CodesnugUser.objects.all().count(), 2)