from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Product)
admin.site.register(RootCategory)
admin.site.register(SubCategory)
admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Size)


