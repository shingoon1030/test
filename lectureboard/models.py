from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone
from django.conf import settings

class lectureB (models.Model) :
    L_CHOICES = (
        ('미선택', '미선택'),
        ('고전역학', '고전역학'),
        ('응용물리탐구', '응용물리탐구'),
        ('프로그래밍', '프로그래밍'),
        ('수학세미나', '수학세미나'),
        ('통합수학', '통합수학'),
        ('에너지환경과학', '에너지환경과학'),
    )
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    title = models.CharField(max_length = 200 )
    titleL = models.CharField(max_length = 200, choices = L_CHOICES)
    titleT = models.CharField(max_length = 200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    hits = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length = 20)
    
    def __str__(self) :
        return self.title

    @property
    def hit_count__(self) :
        self.hits = self.hits+1
        self.save()
        return ""

    @property
    def created_string(self):
        time = datetime.now(tz=timezone.utc) - self.date
        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.date.date()
            return str(time.days) + '일 전'
        else:
            return False
