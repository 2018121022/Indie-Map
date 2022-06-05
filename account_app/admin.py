from django.contrib import admin
from .models import User, Concert, Feedback, Highlight

# Register your models here.

admin.site.register(User)
admin.site.register(Concert)
admin.site.register(Feedback)
admin.site.register(Highlight)