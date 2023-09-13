from django import forms
from posts.models import Post, Comment
from users.models import User

class PostForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all())

    class Meta:
        model = Post
        fields = ['user', 'title', 'content']



class CommentForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), empty_label=None)
    class Meta:
        model = Comment
        fields = ['user', 'comment']

    post_id = forms.IntegerField(widget=forms.HiddenInput())


