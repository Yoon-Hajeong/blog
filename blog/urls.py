from django.urls import path
from . import views
from .views import register, user_login

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('<int:id>', views.blog_detail, name='blog_detail'),
    path('write/', views.post_write, name='post_write'),
    path('edit/<int:id>/', views.post_edit, name='post_edit'),
    path('delete/<int:id>/', views.post_delete, name='post_delete'),
    path('search/<str:tag>/', views.post_search, name='post_search'),
    path('search/', views.post_search, name='post_search'),    
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
]