from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from .models import Post, Comment
from django.shortcuts import get_object_or_404
from .forms import PostForm, CommentForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import *

class post_list(ListView):
  queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
  context_object_name = 'posts'
  template_name = 'blog/post_list.html'

class post_detail(DetailView):
  model = Post
  context_object_name = 'post'
  template_name = "blog/post_detail.html"

class post_new(CreateView):
  model = Post
  template_name = 'blog/post_edit.html'
  form_class = PostForm
  success_url = reverse_lazy('post_list')

  def form_valid(self, form):
    self.object = form.save(self.request.user)
    return HttpResponseRedirect(self.get_success_url())

class post_edit(UpdateView):
  model = Post
  form_class = PostForm
  template_name = 'blog/post_edit.html'
  success_url = reverse_lazy('post_list')

class post_remove(DeleteView):
  model = Post
  template_name = 'blog/post_delete.html'
  success_url = reverse_lazy('post_list')

#  下書き 
class post_draft_list(ListView):
  queryset = Post.objects.filter(published_date__isnull = True).order_by('create_date')
  context_object_name = 'posts'
  template_name = "blog/post_draft_list.html"

# -------------------------------- コメント --------------------------------

class add_comment_to_post(CreateView):
  model = Comment
  form_class = CommentForm
  template_name = 'blog/add_comment_to_post.html'

  def form_valid(self, form):
    comment = form.save(commit=False)
    comment.post = Post.objects.get(id=self.kwargs['pk'])
    comment.save()
    return super().form_valid(form)

  def get_success_url(self):
    return reverse('post_detail', kwargs={'pk': self.object.post.pk})

@login_required
def comment_approve(request, pk):
  comment = get_object_or_404(Comment, pk=pk)
  comment.approve()
  return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
  comment = get_object_or_404(Comment, pk=pk)
  comment.delete()
  return redirect('post_detail', pk=comment.post.pk)

@login_required
def post_publish(request, pk):
  post = get_object_or_404(Post, pk=pk)
  post.publish()
  return redirect('post_detail', pk=pk)
