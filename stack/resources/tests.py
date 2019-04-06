from django.test import TestCase
from .models import Resource
from users.models import Profile


class ResourceTests(TestCase):
	def test_cannot_create_more_resource_than_profile_quota(self):
		profile = Profile.objects.create_user(email='test@test.com', password='tester', quota=1)
		resource1 = Resource.objects.create(profile=profile)
		assert resource1 is not None
		try:
			resource2 = Resource.objects.create(profile=profile)
			assert False
		except:
			assert True