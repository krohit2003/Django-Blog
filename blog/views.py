from django.http import HttpResponse
from django.shortcuts import redirect, render , get_object_or_404

from blog.models import Blog, Category

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