# Generated by Django 3.2.6 on 2021-10-28 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teamchat',
            name='teamid',
        ),
        migrations.AddField(
            model_name='teamchat',
            name='team',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.team'),
            preserve_default=False,
        ),
    ]