# Generated by Django 2.0.5 on 2020-03-02 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0004_auto_20200302_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sreenshots',
            name='screenshots',
            field=models.ImageField(upload_to='static/img'),
        ),
    ]
