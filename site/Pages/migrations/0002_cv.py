# Generated by Django 5.1.1 on 2024-09-12 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cv', models.FileField(max_length=256, upload_to='Files', verbose_name='CV')),
            ],
        ),
    ]
