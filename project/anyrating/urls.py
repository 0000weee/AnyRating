from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name='index'),
 	# path('account/<slug:username>/', views.account_view, name='account'),
	path('<slug:category>', views.index, name='index'),
	path('post/', views.post, name='post'),
	path('profile/<slug:username>/follows/', views.follows, name='follows'),
	path('profile/<slug:username>/followers/', views.followers, name='followers'),
	path('profile/<slug:username>/', views.profile, name='profile'),
]
