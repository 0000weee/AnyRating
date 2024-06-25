from django.db import models
from django.contrib.auth.models import User # account.html

import datetime
# Create your models here.
class Comment(models.Model):
	CATEGORY_CHOICES = {
		('Book', 'Book'),
		('Movie', 'Movie'),
		('Restaurant', 'Restaurant')
	}

	author = models.CharField(max_length=20)
	category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
	title = models.CharField(max_length=20)
	image = models.ImageField(upload_to="images/")
	content = models.TextField(max_length=1000)
	rating = models.IntegerField()
	location = models.CharField(max_length=20, blank=True)
	pub_date = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-rating', 'category', 'author', ]

	def __str__(self):
		return self.author

class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
