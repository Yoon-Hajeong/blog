from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog', views.blog_list, name='blog_list'),
    path('blog/<int:id>', views.blog_detail, name='blog_detail'),
    path('write/', views.post_write, name='post_write'),
]