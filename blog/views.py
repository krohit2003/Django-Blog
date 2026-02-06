from django.http import HttpResponse
from django.shortcuts import redirect, render , get_object_or_404

from blog.models import Blog, Category

from django.db.models import Q

# Create your views here.

def post_by_category(request, pk):
    posts=Blog.objects.filter(category_id=pk)
    # try: 
    #     category= Category.objects.get(id=pk)
    # except:
    #    return redirect('home')
    category = get_object_or_404(Category, id=pk)
    context={
        'posts':posts,
        'category_id': pk,
        'category': category
        }
    
    return render(request, 'post_by_category.html', context)


def blog_details(request , slug):
    single_blog= get_object_or_404(Blog, slug=slug , status='published')

    context={
        'single_blog': single_blog
    } 
    return render(request, 'blog_details.html' , context)


def search(request):
    keyword= request.GET.get('keyword')
    # print(keyword)
    blogs= Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) , status='published')
    # print(blogs)
    # print(type(blogs))
    context={
        'blogs': blogs,
        'keyword': keyword
    }

    return render(request, 'search.html' , context)
