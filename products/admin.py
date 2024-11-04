from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]


# Register your models here.

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
