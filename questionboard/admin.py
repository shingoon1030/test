from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import questionB
from .models import comment



class PostAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(questionB, PostAdmin)
admin.site.register(comment)

