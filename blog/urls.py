from django.urls import path
from . import views

# app_name = 'blog'
urlpatterns = [
    path('', views.post_list.as_view(), name='post_list'),
    path('post/<int:pk>', views.post_detail.as_view(), name='post_detail'),
    path('post/new/', views.post_new.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit.as_view(), name='post_edit'),
    path('post/<pk>/remove/', views.post_remove.as_view(), name='post_remove'),
    # 関数
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),


    # comment
    path('post/<pk>/comment/', views.add_comment_to_post.as_view(), name='add_comment_to_post'),
    # 関数
    path('comment/<pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<pk>/remove/', views.comment_remove, name='comment_remove'),


    # drafts
    path('drafts/', views.post_draft_list.as_view(), name='post_draft_list'),
]
