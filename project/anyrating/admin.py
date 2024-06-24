from django.contrib import admin
from .models import Comment, Profile
from django.contrib.auth.models import User

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
	list_display = ('author', 'category', 'title', 'rating')
	list_filter = ('author', 'category', 'rating')

admin.site.register(Comment, CommentAdmin)

class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    # fields = ["username", "password"]
    list_display = ('username', 'id', )
    inlines = [ProfileInline]

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'id')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)