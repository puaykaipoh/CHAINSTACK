from django.test import TestCase, Client
from django.urls import reverse
from .models import Profile

client = Client()


class UserModelTests(TestCase):
	email = 'test@test.com'
	password = 'tester'

	def test_can_create_user(self):
		profile = Profile.objects.create_user(email=self.email, password=self.password)
		assert profile is not None
		assert Profile.objects.count() > 0

	def test_api_client_login_correct_password(self):
		profile = Profile.objects.create_user(email=self.email, password=self.password)
		response = client.post(reverse('login'), data="email=%s&password=%s" % (self.email, self.password), content_type="application/x-www-form-urlencoded")
		assert response.status_code == 200
		assert 'token' in response.json()

	def test_api_client_login_wrong_password(self):
		profile = Profile.objects.create_user(email=self.email, password=self.password)
		response = client.post(reverse('login'), data="email=%s&password=wrong" % self.email, content_type="application/x-www-form-urlencoded")
		assert response.status_code == 404
		assert 'error' in response.json()