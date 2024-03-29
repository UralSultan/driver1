# Generated by Django 4.0.4 on 2022-05-07 10:05

from django.db import migrations, models
import news.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ('-created_date',), 'verbose_name': 'Новости'},
        ),
        migrations.AddField(
            model_name='news',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=news.models.video_save_path),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=news.models.image_save_path),
        ),
    ]
