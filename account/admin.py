from django.contrib import admin
from account.models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'city', 'date_of_birth']


#admin.site.register(Profile)

