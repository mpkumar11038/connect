from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin
from core.models import User

# Register your models here.
admin.site.register(User)

TokenAdmin.raw_id_fields = ['user']
