from django.contrib import admin
from django import forms
# Register your models here.
from .models import Profile,Friend,ChatMessage


admin.site.register([Profile,Friend])

