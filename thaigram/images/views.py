from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment, Image, Like
from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.


def index_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            # user = request.user
            # comments_by_user = user.comment_set.all()
            # images_by_user = user.image_set.all()
            # likes_by_user = user.like_set.all()
            # print(comments_by_user, images_by_user, likes_by_user)
            all_images = Image.objects.all()
            return render(request, 'feed.html', context={'all_images': all_images})
        else:
            return render(request, 'login.html')


def explore_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            
            all_users = User.objects.all()
            return render(request, 'explore.html', context={'all_users': all_users})
        else:
            return render(request, 'login.html')
    

def profile_view(request):
    if request.method == "GET":
        if request.user.is_authenticated:

            my_images = request.user.image_set.all()
            return render(request, 'profile.html', context={'my_images': my_images, 'user': request.user})
        else:
            return render(request, 'login.html')
