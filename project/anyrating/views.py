from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment, Profile
from django.contrib.auth.decorators import login_required # account.html
from .forms import CommentForm
from django.contrib.auth.models import User

# Create your views here.
def index(request, category=''):
	notFound = 0
	friend = 0
	profile = {}
	if request.method == "POST":
		keyword = request.POST.get('keyword')
		friend_only = request.POST.get('friend_only')

		if category == '':
			comments = Comment.objects.filter(title__contains=keyword)
			if not comments.exists():
				notFound = 1
				comments = Comment.objects.all()
			elif friend_only == "yes":
				friend = 1
				profile = Profile.objects.get(user=request.user)
				for comment in comments:
					comment.dummy = Profile.objects.get(user=User.objects.get(username=comment.author))
		else:
			comments = Comment.objects.filter(category__exact=category, title__contains=keyword)
			if not comments.exists():
				notFound = 1
				comments = Comment.objects.filter(category__exact=category)
			elif friend_only == "yes":
				friend = 1
				profile = Profile.objects.get(user=request.user)
				for comment in comments:
					comment.dummy = Profile.objects.get(user=User.objects.get(username=comment.author))
	else:
		if category == '':
			comments = Comment.objects.all()
		else:
			comments = Comment.objects.filter(category__exact=category)

	context = {
		'comments': comments,
		'notFound': notFound,
		'profile': profile,
		"friend": friend,
	}
	return render(request, "index.html", context=context)

# account.html
# views.py
@login_required
def account_view(request, username=''):
    user = request.user
    profile = Profile.objects.get(user=request.user)
    context = {
        'user': user,
        # 假設你有一個相關的 Post 模型
        'posts': user.posts.all(),  # 假設 User 模型有一個 posts 關聯
        'username': username,
        'profile': profile,
    }
    return render(request, 'account.html', context)

def profile(request, username):
	profile = Profile.objects.get(user=request.user)

	cur_user = User.objects.get(username=username)
	cur_user_profile = Profile.objects.get(user=cur_user)

	if request.method == "POST":
		data = request.POST
		action = data.get("follow")
		
		if action == "follow":
			profile.follows.add(cur_user_profile)
		elif action == "unfollow":
			profile.follows.remove(cur_user_profile)

		profile.save()

	comments = Comment.objects.filter(author__exact=username)

	context = {
		'user': request.user,
		'profile': profile,
		'cur_user': cur_user,
		'cur_user_profile': cur_user_profile,
		'comments': comments,
	}

	return render(request, "profile.html", context=context)

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

def follows(request, username):
	cur_user = User.objects.get(username=username)
	profile = Profile.objects.get(user=cur_user)
	context={
		"profile": profile,
	}

	return render(request, "follows.html", context=context)

def followers(request, username):
	cur_user = User.objects.get(username=username)
	profile = Profile.objects.get(user=cur_user)
	context={
		"profile": profile,
	}

	return render(request, "followers.html", context=context)
	