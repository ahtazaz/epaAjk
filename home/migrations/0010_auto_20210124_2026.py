# Generated by Django 3.1.5 on 2021-01-24 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='air',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
