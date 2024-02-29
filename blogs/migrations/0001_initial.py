# Generated by Django 5.0.1 on 2024-02-29 20:01

import django.db.models.deletion
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
                ('header', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('text', models.TextField()),
                ('instagram', models.TextField()),
                ('twitter', models.TextField()),
                ('slug', models.SlugField()),
                ('image', models.ImageField(upload_to='blog/')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
                ('comment', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog/')),
                ('published', models.BooleanField(default=False)),
                ('blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blogs.blog')),
            ],
        ),
    ]
