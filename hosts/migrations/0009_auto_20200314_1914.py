# Generated by Django 2.0.5 on 2020-03-14 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0008_auto_20200313_2304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='logs',
            name='categories',
            field=models.ManyToManyField(to='hosts.Category'),
        ),
        migrations.AddField(
            model_name='sreenshots',
            name='categories',
            field=models.ManyToManyField(to='hosts.Category'),
        ),
    ]
