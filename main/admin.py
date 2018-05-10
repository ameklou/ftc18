from django.contrib import admin
from .models import Author, Project
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class AuthorAdmin(SummernoteModelAdmin):
    list_display = ('name','slug', 'city', 'profession',)
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Author, AuthorAdmin)


class ProjectAdmin(SummernoteModelAdmin):
    list_display = ('title','author', 'link','slug')
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Project, ProjectAdmin)
