from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import freeB
from .models import comment



class PostAdmin(SummernoteModelAdmin):
    summernote_fields = 'body'

admin.site.register(freeB, PostAdmin)
admin.site.register(comment)

