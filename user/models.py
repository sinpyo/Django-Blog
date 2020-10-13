from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, nickname, password=None):
        if not email:
            raise ValueError('must have user email')
        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password):
        user = self.create_user(
            email=self.normalize_email(email),
            nickname=nickname,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    GENDER_CHOICES = {
        ('male', '남'),
        ('female', '여'),
        ('not-specified', 'Not Specified')
    }
    INTEREST_CHOICES = {
        ('한식', '한식'),
        ('중식', '중식'),
        ('양식', '양식'),
        ('일식', '일식')
    }

    email = models.EmailField(max_length=100, unique=True, verbose_name="e-mail")
    nickname = models.CharField(max_length=20, null=False, unique=True, verbose_name="Nick Name(별명)")
    last_name = models.CharField(max_length=10, null=False, verbose_name="Last Name(성)")
    first_name = models.CharField(max_length=20, null=False, verbose_name="First Name(이름)")
    birth_date = models.DateField(null=True, blank=True, verbose_name="생년월일")
    gender = models.CharField(max_length=50, null=False, choices=GENDER_CHOICES, verbose_name="성별")
    interest_part = models.CharField(max_length=50, null=True, choices=INTEREST_CHOICES, verbose_name="관심 요리 분야")
    is_active = models.BooleanField(default=True, verbose_name="활성화 여부")
    is_admin = models.BooleanField(default=False, verbose_name="관리자 여부")
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
#    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = ['email']
