from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post, Comment, User
from posts.forms import PostForm, CommentForm


def list_social_network(request):
    users = User.objects.all()
    posts = Post.objects.all()
    comments = Comment.objects.all()
    context = {
        'users': users,
        'posts': posts,
    }
    return render(request, 'posts/social_network_list.html', context)


# def list_comments(request):


def add_post(request):
    if request.method == 'POST':
        print(str(5) * 100)
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('user_detail', user_id=post.user.id)
    else:
        form = PostForm()
    return render(request, 'posts/add_post.html', {'form': form})


# def add_comment(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     print(post_id)
#     print(request.method)
#     print(str(66) * 100)
#     if request.method == 'POST':
#         print(str(67) * 100)
#         form = CommentForm(request.POST, request.FILES)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.save()
#             return redirect('post_detail', user_id=post.id)
#     else:
#         form = CommentForm()
#     return render(request, 'posts/add_comment.html', {'form': form})
def add_comment(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES, initial={'post_id': post_id})
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm(initial={'post_id': post_id})
    return render(request, 'posts/add_comment.html', {'form': form})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    users = User.objects.filter(pk=post_id)
    comments = Comment.objects.filter(post=post_id)
    context = {
               'users': users,
               'comments': comments,
               'post': post
    }
    return render(request, 'posts/post_detail.html', context)