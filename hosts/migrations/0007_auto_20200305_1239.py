# Generated by Django 2.0.5 on 2020-03-05 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0006_auto_20200302_1618'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Host',
        ),
        migrations.AddField(
            model_name='logs',
            name='description',
            field=models.CharField(default=None, max_length=100000000),
        ),
        migrations.AddField(
            model_name='logs',
            name='ip_source',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='sreenshots',
            name='ip_source',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='logs',
            name='plaintext',
            field=models.CharField(max_length=1000000000, null=True),
        ),
        migrations.AlterField(
            model_name='sreenshots',
            name='description',
            field=models.CharField(default=None, max_length=100000000),
        ),
    ]
