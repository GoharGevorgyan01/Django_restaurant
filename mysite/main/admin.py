from django.contrib import admin
from .models import HomeReference,Recipes,About,Blog,Contact

# Register your models here.

admin.site.register(HomeReference)
@admin.register(Recipes)
class RecipeseAdmin(admin.ModelAdmin):
    list_display=['id','name']
    list_display_links=['id','name']
    search_fields=['name']

admin.site.register(About)
admin.site.register(Blog)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=['id','name','email']
    list_display_links=['id','name']
    search_fields=['name']
