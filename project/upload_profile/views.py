# Create your views here.
from django.shortcuts import render
# Create your views here.
def add(request):
    
    return render(request, 'upload_profile/add.html', locals())
def detail(request):
    return render(request, 'upload_profile/detail.html', locals())