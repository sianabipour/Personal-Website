# Generated by Django 5.0.1 on 2024-02-26 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0010_experience_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='category',
        ),
        migrations.AddField(
            model_name='skill',
            name='category',
            field=models.CharField(default='ss', max_length=100),
            preserve_default=False,
        ),
    ]
