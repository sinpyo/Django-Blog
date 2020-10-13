# Generated by Django 3.0.8 on 2020-08-05 19:31

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='e-mail')),
                ('nickname', models.CharField(max_length=20, unique=True, verbose_name='Nick Name(별명)')),
                ('last_name', models.CharField(max_length=10, verbose_name='Last Name(성)')),
                ('first_name', models.CharField(max_length=20, verbose_name='First Name(이름)')),
                ('birth_date', models.DateField(null=True, blank=True, verbose_name='생년월일')),
                ('gender', models.CharField(choices=[('male', '남'), ('not-specified', 'Not Specified'), ('female', '여')], max_length=50, verbose_name='성별')),
                ('interest_part', models.CharField(choices=[('중식', '중식'), ('한식', '한식'), ('양식', '양식'), ('일식', '일식')], max_length=50, null=True, verbose_name='관심 요리 분야')),
                ('is_active', models.BooleanField(default=True, verbose_name='활성화 여부')),
                ('is_admin', models.BooleanField(default=False, verbose_name='관리자 여부')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', user.models.UserManager()),
            ],
        ),
    ]