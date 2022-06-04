from django.contrib import admin
from .models import Film

class TboxdAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')

# Register your models here.

admin.site.register(Film, TboxdAdmin)