from django.contrib import admin
from .models import User, Concert

# Register your models here.

admin.site.register(User)
admin.site.register(Concert)