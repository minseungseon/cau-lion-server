# Generated by Django 2.1.1 on 2020-05-15 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homework_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
