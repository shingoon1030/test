from django import forms
from django.forms import TextInput
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class lectureBForm(forms.Form) :
    L_CHOICES = (
        ('미선택', '미선택'),
        ('고전역학', '고전역학'),
        ('응용물리탐구', '응용물리탐구'),
        ('프로그래밍', '프로그래밍'),
        ('수학세미나', '수학세미나'),
        ('통합수학', '통합수학'),
        ('에너지환경과학', '에너지환경과학'),
    )
    title = forms.CharField(widget=TextInput(attrs={'style' : 'width: 800px; margin-left:3%; height: 50px; border-radius: 0.3rem;'}))
    titleL = forms.ChoiceField(choices=L_CHOICES)
    titleT = forms.CharField()
    body = forms.CharField(widget=SummernoteWidget(attrs={'style' : 'width: 100%;  height: 500px;'}))
