# Generated by Django 2.0.5 on 2020-03-14 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0012_auto_20200314_1937'),
    ]

    operations = [
        migrations.RenameField(
            model_name='source',
            old_name='ip_source',
            new_name='source',
        ),
        migrations.AlterField(
            model_name='team',
            name='team',
            field=models.CharField(choices=[('Red', 'Red'), ('Blue', 'Blue')], max_length=5),
        ),
    ]