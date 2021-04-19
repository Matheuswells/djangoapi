from django.test import TestCase
from blog.models import User, Post

class  UserTestCase(TestCase):
    newUser: User 
    def setUp(self):
        newUser = User.objects.create(username="userTest", name="User", last_name="Resu", birthday="1999-12-10")

    def testUsers(self):
        userTest = User.objects.get(username="userTest")
        self.assertEqual(userTest.username,"userTest")