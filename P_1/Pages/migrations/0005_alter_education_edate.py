# Generated by Django 5.0.1 on 2024-02-25 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0004_alter_education_edate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='edate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
