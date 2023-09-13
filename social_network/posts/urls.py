from django.urls import path

from .views import list_social_network, add_post, post_detail, add_comment
from users.views import add_user, user_list, user_detail

urlpatterns = [
    path('', list_social_network, name='list_social_network'),
    path('users/add_user', add_user, name='add_user'),
    path('users/', user_list, name='user_list'),
    path('users/<int:user_id>', user_detail, name='user_detail'),
    path('posts/<int:post_id>', post_detail, name='post_detail'),
    path('posts/<int:post_id>/add_comment/', add_comment, name='add_comment'),
    path('add_post/', add_post, name='add_post')
]
