# Generated by Django 3.2.7 on 2021-10-23 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20211023_2316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teamchat',
            old_name='author',
            new_name='menber',
        ),
    ]