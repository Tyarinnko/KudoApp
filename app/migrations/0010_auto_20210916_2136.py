# Generated by Django 2.0.2 on 2021-09-16 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_delete_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]