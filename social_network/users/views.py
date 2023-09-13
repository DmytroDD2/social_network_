from django.shortcuts import render, redirect, get_object_or_404
from users.models import User
from posts.models import Post, Comment
from users.forms import UserForm

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect('user_detail', user_id=user.pk)
    else:
        form = UserForm()
    return render(request, 'posts/add_user.html', {'form': form})


def user_list(request):
    users = User.objects.all()
    context = {'users': users, 'list': 'List of users'}
    return render(request, 'posts/users_list.html', context)


def user_detail(request, user_id):
    userr = get_object_or_404(User, pk=user_id)
    posts = Post.objects.filter(user=user_id)
    comments = Comment.objects.filter(user=user_id)
    context = {
               'userr': userr,
               'comments': comments,
               'posts': posts
    }
    return render(request, 'posts/user_detail.html', context)