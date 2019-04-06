from django.test import TestCase
from .models import Profile


class UserModelTests(TestCase):
	def test_can_create_user(self):
		profile = Profile.objects.create_user(email='test@test.com', password='tester')
		assert profile is not None
		assert Profile.objects.count() > 0
