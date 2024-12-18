from django.contrib import admin
from .models import Post, Contact, Services, SocialNetworks, Employees, Gallery, Reviews

# Register your models here.
admin.site.register({Post, Contact, Services, SocialNetworks, Employees, Gallery, Reviews})
