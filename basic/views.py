from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Blog, Mentee, Mentor
from django.urls import reverse
# Create your views here.

def index(request):
    return render(request, 'basic/index.html', {})

def blog(request):
    blog = Blog.objects.all()
    return render(request, 'basic/blog.html', {'blog': blog})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'basic/detail.html', {'blog': blog})


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
    image_path = request.POST['image_path']
    blog_title = request.POST['blog_title']
    blog_content = request.POST['blog_content']

    bl = Blog(image_path=image_path, blog_title=blog_title, blog_content=blog_content)
    bl.save()
    blog = Blog.objects.all()
    
    return render(request,'basic/blog.html', {'blog': blog}) 
