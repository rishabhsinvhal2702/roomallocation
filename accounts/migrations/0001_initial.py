# Generated by Django 3.2.11 on 2022-01-20 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('rollno', models.CharField(max_length=10, unique=True)),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('email', models.EmailField(max_length=60, unique=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=51)),
                ('last_name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
