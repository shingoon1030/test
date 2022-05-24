from django import forms
from django.forms import TextInput
from .models import comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class questionBForm(forms.Form) :
    Q_CHOICES = (
        ('미선택', '미선택'),
        ('고전역학', '고전역학'),
        ('응용물리탐구', '응용물리탐구'),
        ('프로그래밍', '프로그래밍'),
        ('수학세미나', '수학세미나'),
        ('통합수학', '통합수학'),
        ('에너지환경과학', '에너지환경과학'),
    )
    title = forms.CharField(widget=TextInput(attrs={'style' : 'width: 800px; margin-left:3%; height: 50px; border-radius: 0.3rem;'}))
    titleQ = forms.ChoiceField(choices=Q_CHOICES)
    body = forms.CharField(widget=SummernoteWidget(attrs={'style' : 'width: 100%;  height: 500px;'}))


class commentForm(forms.ModelForm) :
    comment = forms.CharField(widget=TextInput(attrs={'style' : 'width: 600px; margin-left:1%; height: 40px; border-radius: 0.3rem;'}))
    class Meta:
        model = comment
        fields =  ['comment']
