# Generated by Django 4.2.5 on 2024-03-27 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBlogApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
