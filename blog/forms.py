from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
  
  class Meta:
    model = Post
    fields = ['title', 'text']

  def save(self, user):
    obj = super().save(commit=False)
    obj.author = user
    obj.save()
    return obj


class CommentForm(forms.ModelForm):
  
  class Meta:
    model = Comment
    fields = ['author', 'text']