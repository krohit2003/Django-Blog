
from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Category , Blog

from assignments.models import About
def home(request):
    
    featured_posts=Blog.objects.filter(is_featured=True , status='published')
    post=Blog.objects.filter(is_featured=False , status='published')

    try:
        about=About.objects.get()
    except:
        about=None    
    

    context={
       
        'featured_posts':featured_posts,
        'post':post,
        'about':about
    }

    return render(request , 'home.html' , context)