from django.test import TestCase, Client
from django.urls import reverse
from .models import Resource
from users.models import Profile

client = Client()

class ResourceTests(TestCase):
	email = 'test@test.com'
	password = 'tester'
	quota = 1

	def create_profile(self):
		return Profile.objects.create_user(email=self.email, password=self.password, quota=self.quota)

	def create_profile_and_resource(self):
		profile = self.create_profile()
		return Resource.objects.create(profile=profile)

	def get_login_token(self):
		response = client.post(reverse('login'), data="email=%s&password=%s" % (self.email, self.password), content_type="application/x-www-form-urlencoded")
		assert response.status_code == 200
		assert 'token' in response.json()
		return response.json().get('token')

	def test_cannot_create_more_resource_than_profile_quota(self):
		resource1 = self.create_profile_and_resource()
		assert resource1 is not None
		try:
			resource2 = Resource.objects.create(profile=profile)
			assert False
		except:
			assert True

	def test_api_list_resource(self):
		resource1 = self.create_profile_and_resource()
		assert resource1 is not None
		token = self.get_login_token()
		headers = {'HTTP_AUTHORIZATION':'Token %s' % token}
		response = client.get(reverse('resource'), content_type="application/x-www-form-urlencoded", **headers)
		assert response.status_code == 200
		assert len(response.json()) == 1

	def test_api_create_resource(self):
		profile = self.create_profile()
		assert profile is not None
		token = self.get_login_token()
		headers = {'HTTP_AUTHORIZATION':'Token %s' % token}
		response = client.put(reverse('resource'), content_type="application/x-www-form-urlencoded", **headers)
		assert 'id' in response.json()
		assert response.status_code == 200
		response = client.get(reverse('resource'), content_type="application/x-www-form-urlencoded", **headers)
		assert response.status_code == 200
		assert len(response.json()) == 1

	def test_api_delete_resource(self):
		resource1 = self.create_profile_and_resource()
		assert resource1 is not None
		token = self.get_login_token()
		headers = {'HTTP_AUTHORIZATION':'Token %s' % token}
		response = client.delete(reverse('resource'), data="id=%s"%resource1.id,content_type="application/x-www-form-urlencoded", **headers)
		assert str(response.json().get('id')) == str(resource1.id)
		assert response.status_code == 200
		response = client.get(reverse('resource'), content_type="application/x-www-form-urlencoded", **headers)
		assert response.status_code == 200
		assert len(response.json()) == 0
