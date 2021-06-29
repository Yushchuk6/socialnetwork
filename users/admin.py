from django import forms
from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


# class UserAdminForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = "__all__"


# class UserAdmin(admin.ModelAdmin):
#     form = UserAdminForm


admin.site.register(User, UserAdmin)
