from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
	#get all my posts from the database
	posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
	return render(request,'blog/post_list.html', { 'posts' : posts }) #{'posts':posts} -> {'key':value}

def joke(request):
	return render(request,'blog/ciccc.html')
