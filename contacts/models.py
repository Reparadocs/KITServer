from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
	owner = models.ForeignKey(User)
	name = models.CharField(max_length=100)
	phone = models.CharField(max_length=100, blank=True)
	email = models.CharField(max_length=100, blank=True)
	reminder = models.IntegerField()
	last = models.DateTimeField(auto_now_add=True)
