from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Articles

# Register your models here.


class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    summernote_field = '__all__'


admin.site.register(Articles, PostAdmin)

