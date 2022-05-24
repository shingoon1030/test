from django.conf import settings
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self, username, password, email, time_table):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            time_table=time_table,
        )
        user.is_admin = False
        user.is_superuser = False
        user.is_staff = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, email, time_table=None):
        user = self.create_user(username,password,email,time_table)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    objects = UserManager()

    username = models.CharField(max_length=17, verbose_name="아이디", unique=True)
    password = models.CharField(max_length=256, verbose_name="비밀번호")
    email = models.EmailField(max_length=128, verbose_name="이메일", unique=True)
    time_table = models.CharField(max_length=1024, verbose_name="시간표", null=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

class UserBackend(object):
    def authenticate(self, username=None, password=None):
        if check_if_user(username, password): 
            try: 
                user = UserModel.objects.get(username=username)
                return user
            except UserModel.DoesNotExist: 
                print("error")
                return None
            
        