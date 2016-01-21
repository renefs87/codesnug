from django.test import TestCase

# Create your tests here.
from codesnug_2.auth.models import CodesnugUser
from codesnug_2.goals.models import Tag


class TagTestCase(TestCase):
    def setUp(self):
        self.user = CodesnugUser.objects.create_user('prueba@prueba.com', '1111')
        self.user2 = CodesnugUser.objects.create_user('prueba2@prueba2.com', '1111')

        Tag.objects.create(title="tag1", owner=self.user)
        Tag.objects.create(title="tag2", owner=self.user2)

    def test_create_tags(self):
        tag1 = Tag.objects.get(title="tag1")
        tag2 = Tag.objects.get(title="tag2")
        self.assertIsNotNone(tag1)
        self.assertIsNotNone(tag2)
