from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Blog_type)
admin.site.register(Blog)
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(Competition)
admin.site.register(Competitors)