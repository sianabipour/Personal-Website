# Generated by Django 3.2 on 2023-10-15 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=180)),
                ('date', models.DateField()),
                ('image', models.ImageField(upload_to='blog/')),
                ('content', models.TextField()),
            ],
        ),
    ]
