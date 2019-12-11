from django.contrib import admin
from django.urls import path
from . import views

app_name = 'basic'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('blog', views.blog, name = 'blog'),
    path('blog/<int:blog_id>/', views.detail, name='detail'),
    path('mentor', views.mentor, name = 'mentor'),
    path('mentee', views.mentee, name = 'mentee'),
    path('author', views.author, name = 'author'),
    path('input_content', views.input_content, name='input_content'),
    path('save_content', views.save_content, name='save_content')
]