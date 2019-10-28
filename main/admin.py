from django.contrib import admin
from .models import UserProfile,Entry,Comment,Star

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Entry)
admin.site.register(Comment)
admin.site.register(Star)
