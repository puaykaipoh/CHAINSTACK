import uuid
import threading
from django.db import models
from users.models import Profile

lock = threading.Lock()

# Create your models here.
class Resource(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='resources')

	def save(self, *args, **kwargs):
		lock.acquire()
		try:
			if self.profile.quota:
				if self.profile.resources.count() >= self.profile.quota:
					raise Exception('Number of resource more than quota') # TODO show nice message?
			super(Resource, self).save(*args, **kwargs)
		except:
			lock.release()
		lock.release()