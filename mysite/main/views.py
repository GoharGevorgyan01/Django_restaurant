from django.shortcuts import render,redirect
from .models import HomeReference,Recipes,About,Blog,Contact
# Create your views here.
def index(request):
    home_reference = HomeReference.objects.all()
    recipes = Recipes.objects.all()
    about = About.objects.all()[0]
    blog = Blog.objects.all()
    return render(request,'index.html',context={
        'home_reference':home_reference,
        'recipes':recipes,
        'about':about,
        'blog':blog
    })



def about(request):
    about = About.objects.all()[0]
    return render(request,'about.html',context={
        'about':about
        })

def blog(request):
    blog = Blog.objects.all()
    return render(request,'blog.html',context={
        'blog':blog
    })

def recipe(request):
    recipes = Recipes.objects.all()
    return render(request,'recipe.html',context=
                  {'recipes':recipes
                   })

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        review = request.POST.get('review')
        Contact.objects.create(name = name,email=email,phone=phone,review=review)
        return redirect('index')
    return render(request,'contact.html')