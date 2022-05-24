from django import forms
from django.forms import TextInput
from .models import comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class freeBForm(forms.Form) :
    title = forms.CharField(widget=TextInput(attrs={'style' : 'width: 800px; margin-left:3%; height: 50px; border-radius: 0.3rem;'}))
    body = forms.CharField(widget=SummernoteWidget(attrs={'style' : 'width: 100%;  height: 500px;'}))


class commentForm(forms.ModelForm) :
    comment = forms.CharField(widget=TextInput(attrs={'style' : 'width: 600px; margin-left:1%; height: 40px; border-radius: 0.3rem;'}))
    class Meta:
        model = comment
        fields =  ['comment']
