# Generated by Django 2.0.5 on 2020-03-14 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0009_auto_20200314_1914'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_source', models.CharField(max_length=16)),
            ],
        ),
        migrations.RemoveField(
            model_name='logs',
            name='ip_source',
        ),
        migrations.RemoveField(
            model_name='sreenshots',
            name='ip_source',
        ),
        migrations.AddField(
            model_name='logs',
            name='ip_source',
            field=models.ManyToManyField(to='hosts.Source'),
        ),
        migrations.AddField(
            model_name='sreenshots',
            name='ip_source',
            field=models.ManyToManyField(to='hosts.Source'),
        ),
    ]