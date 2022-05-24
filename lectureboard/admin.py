from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import lectureB
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(lectureB, PostAdmin)

