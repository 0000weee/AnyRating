from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
	CATEGORY_CHOICES = {
		('Book', 'Book'),
		('Movie', 'Movie'),
		('Restaurant', 'Restaurant')
	}

	author = forms.CharField(max_length=20, widget=forms.TextInput(attrs={"type": "hidden"}))
	title = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'mb-2', "id": "title"}))
	category = forms.ChoiceField(choices=CATEGORY_CHOICES, widget=forms.Select(attrs={'class': 'mb-2', 'id': 'category'}))
	image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'mb-2', 'id': 'image'}))
	content = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class': 'comment_textarea mb-2', 'rows': 3, 'id': 'comment'}))
	rating = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'mb-2', 'type': 'range', "min": "1", "max": "5", "id": 'rating'}))

	class Meta:
		model = Comment
		fields = ['title', 'category', 'image', 'content', 'rating']
