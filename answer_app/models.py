from django.db import models
from django import forms

# Create your models here.
class Question(models.Model):
	"""A question which a user has submitted"""
	question = models.TextField(max_length = 1000,)
	user_email = models.CharField( max_length = 50)
	date_added = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		"""Return a string representation of the model."""
		return self.text
