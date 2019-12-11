from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Blog, Mentee, Mentor
from django.urls import reverse
# Create your views here.

def index(request):
    return render(request, 'basic/index.html', {})

def blog(request):
    blog = Blog.objects.all()
    return render(request, 'basic/blog.html', {'blog': blog})

def mentor(request):
    mentor = Mentor.objects.all()
    return render(request, 'basic/mentor.html', {'mentor': mentor})

def mentee(request):
    mentee = Mentee.objects.all()
    return render(request, 'basic/mentee.html', {'mentee': mentee})

def author(request):
    return render(request, 'basic/author.html', {})

def input_content(request):
    return render(request, 'basic/input_content.html', {})

def save_content(request):
    img_path = request.POST['img_path']
    blog_title = request.POST['title']
    blog_content = request.POST['blog_content']

    bl = Blog(img_path=img_path, blog_title = blog_title, blog_content=blog_content)
    bl.save()
    blog = Blog.objects.all()
    
    return render(request,'basic/blog.html', {'blog': blog}) 
