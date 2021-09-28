# Generated by Django 3.2.6 on 2021-09-28 02:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20210928_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='image/')),
            ],
        ),
        migrations.AddField(
            model_name='map',
            name='image',
            field=models.OneToOneField(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='app.image'),
            preserve_default=False,
        ),
    ]
