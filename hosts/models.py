from __future__ import unicode_literals

from django.db.models import CharField
from djongo import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Source(models.Model):
    source = models.CharField(max_length=16, null=True)
    player = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.source


class Team(models.Model):
    select_team = (
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('White', 'White'),
    )

    team = models.CharField(max_length=5, choices=select_team)
    players = models.ManyToManyField(User)

    def __str__(self):
        return self.team


class Sreenshots(models.Model):
    # Auto updated when data is inserted
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    # Auto updated when data is altered
    update_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    img = models.ImageField(upload_to='static/img')

    # source -> on to many with hosts
    ip_source = models.ForeignKey(Source, on_delete=models.CASCADE, null=True)

    description = models.CharField(max_length=100000000, default=None, blank=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)


class Logs(models.Model):
    # Auto updated when data is inserted
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    # Auto updated when data is altered
    update_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    plaintext = models.CharField(max_length=1000000000, null=True)
    # source -> on to many with hosts
    ip_source = models.ForeignKey(Source, on_delete=models.CASCADE, null=True)
    #
    description = models.CharField(max_length=100000000, default=None, blank=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.plaintext


class Trainings(models.Model):
    # Auto updated when data is inserted
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    # Auto updated when data is altered
    update_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    img = models.ImageField(upload_to='static/img')

    description = models.CharField(max_length=100000000, default=None, blank=True)
