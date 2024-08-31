from django.contrib import admin
from .models import Slideshow,Service


# Register your models here.

@admin.register(Slideshow)
@admin.register(Service)

class SlideshowAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

