from blog.models import Category  

category= Category.objects.get(id=7)

print(category.category_name)