# Generated by Django 2.1.1 on 2020-05-15 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homework_api', '0003_post_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='user',
        ),
    ]