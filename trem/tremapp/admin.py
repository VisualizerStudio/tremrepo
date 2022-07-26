from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header = 'Trem | Valley Estate'
admin.site.register(Post)