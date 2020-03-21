from django.db import models
from django.contrib.auth.models import User

MOOD_CHOICES = (
	('VH', 'Very Happy'),
	('H', 'Happy'),
	('N', 'Neutral'),
	('S', 'Sad'),
	('VS', 'Very Sad'),
	('A', 'Angry'))

# Create your models here.
class Topic(models.Model):
	"""A topic the user is learning about."""
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(
		User,
		on_delete=models.CASCADE)

	def __str__(self):
		"""Return a string representation of the model."""
		return self.text


class Entry(models.Model):
	"""Journal entry about a topic."""
	title = models.CharField(
		max_length=200,
		default='Uknown title')
	
	mood = models.CharField(
		max_length=12,
		choices=MOOD_CHOICES,
		default='Neutral'
		)

	topic = models.ForeignKey(
		Topic,
		on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		"""Return a string representation of the model."""
		if len(self.text) > 50:
			return self.text[:50]+"..."
		else:
			return self.text
		#return self.title

on_delete=models.CASCADE