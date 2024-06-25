from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name='index'),
 	path('account/', views.account_view, name='account'),
	path('<slug:category>', views.index, name='index'),
	path('post/', views.post, name='post'), 
]
