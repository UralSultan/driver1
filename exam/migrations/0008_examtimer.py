# Generated by Django 4.0.3 on 2022-04-13 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0007_alter_answer_comment_for_right_answer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamTimer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_to_exam', models.IntegerField(default=40)),
            ],
        ),
    ]
