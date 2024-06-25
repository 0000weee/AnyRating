from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment
from django.contrib.auth.decorators import login_required # account.html
from .forms import CommentForm

# Create your views here.
def index(request, category = ''):
	notFound = 0
	if request.method == "POST":
		keyword = request.POST.get('keyword')
		if category == '':
			comments = Comment.objects.filter(title__contains=keyword)
			if not comments.exists():
				notFound = 1
				comments = Comment.objects.all()
		else:
			comments = Comment.objects.filter(category__exact=category, title__contains=keyword)
			if not comments.exists():
				notFound = 1
				comments = Comment.objects.filter(category__exact=category)
	else:
		if category == '':
			comments = Comment.objects.all()
		else:
			comments = Comment.objects.filter(category__exact=category)

	context = {
		'comments': comments,
		'notFound': notFound,
	}
	return render(request, "index.html", context=context)

# account.html
# views.py

@login_required
def account_view(request):
    user = request.user
    context = {
        'user': user,
        # 假設你有一個相關的 Post 模型
        'posts': user.posts.all()  # 假設 User 模型有一個 posts 關聯
    }
    return render(request, 'account.html', context)

def post(request):
	if request.method == "POST":
		author = request.POST.get('author')
		title = request.POST.get('title')
		category = request.POST.get('category')
		image = request.FILES.get('image')
		comment = request.POST.get('comment')
		rating = request.POST.get('rating')

		comment_obj = Comment.objects.create(author=author, category=category, title=title, image=image, content=comment, rating=rating)
		comment_obj.save()

		# form = CommentForm(request.POST, request.FILES)
		# if form.is_valid():
		# 	form.save()
			
		# 	form = CommentForm()
		# 	context = {'form': form}

		# 	return render(request, 'post.html', context=context)
	# else:
	# 	form = CommentForm()

	context = {}
	return render(request, 'post.html', context=context)