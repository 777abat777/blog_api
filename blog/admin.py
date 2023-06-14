from django.contrib import admin
from . import models
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display=["title","id","status","slug","author"]
    prepopulated_fields={"slug":("title",),} # prepopulated_fields - предварительно заполненныеполя
admin.site.register(models.Post,AuthorAdmin)



admin.site.register(models.Category)