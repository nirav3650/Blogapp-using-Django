# Generated by Django 2.0.5 on 2018-05-16 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='blog_description',
            field=models.TextField(null=True),
        ),
    ]
