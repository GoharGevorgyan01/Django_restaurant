from django.db import models

# Create your models here.

class HomeReference(models.Model):
    reference = models.TextField('Home reference',max_length=500)
    info = models.TextField('Home info',max_length=1000)
    img = models.ImageField('Home main img',upload_to='Photo')
   
    def __str__(self):
        return self.reference
    
class Recipes(models.Model):
    name = models.CharField('Product name',max_length=100)
    price = models.PositiveIntegerField('Product price')
    img = models.ImageField('Image',upload_to= 'Photo')

    def __str__(self):
        return self.name

class About(models.Model):
    aboutt = models.TextField('About',max_length=200)
    best_food = models.TextField('Best food',max_length=1500)
    img = models.ImageField('Image',upload_to= 'Photo')


class Blog(models.Model):
    img = models.ImageField('Image',upload_to= 'Photo')
    name = models.CharField('Product name',max_length=100)
    food = models.TextField('food',max_length=1500)
    date = models.CharField('Date',max_length=30)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField('User name',max_length=100)
    email = models.EmailField('Email')
    phone = models.TextField('Phone number',max_length=20)
    review = models.TextField('Review',max_length=400)

    def __str__(self):
        return self.name



    


# class HomeName(models.Model):
#     nam