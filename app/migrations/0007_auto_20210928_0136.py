# Generated by Django 3.2.6 on 2021-09-27 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_map_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='title',
        ),
        migrations.AlterField(
            model_name='map',
            name='image',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.image', verbose_name='写真'),
        ),
    ]
