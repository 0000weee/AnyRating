from django.db import models
from django.contrib.auth.models import User # account.html
from django.db.models.signals import post_save
from django.dispatch import receiver

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
	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to="images/")
	content = models.TextField(max_length=1000)
	rating = models.IntegerField()
	location = models.CharField(max_length=20, blank=True)
	pub_date = models.DateTimeField(auto_now_add=True)
	dummy = models.CharField(max_length=100, blank=True)

	class Meta:
		ordering = ['-rating', 'category', 'author', ]

	def __str__(self):
		return self.author

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False,
        blank=True
    )

    def __str__(self):
        return self.user.username

# Create a Profile for each new user.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.add(instance.profile)
        user_profile.save()
