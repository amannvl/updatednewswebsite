from datetime import datetime
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.forms import DateField
from time import gmtime, strftime




class newslist(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, default="")
    image = models.URLField(null=True, blank=True, default="")
    publishedAt = models.DateField(blank=True, null=True, default="datetime.date.today()")
    description = models.TextField()
    content = models.TextField()
    url = models.URLField(default="")
    author = models.CharField(max_length=50, default="",null=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name

class Newscatwise(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, default="")
    image = models.URLField(null=True, blank=True, default="")
    publishedAt = models.DateField(blank=True, null=True, default="datetime.date.today()")
    category = models.CharField(max_length=100,default="")
    description = models.CharField(max_length=280,default="Not Available Now",null=True)
    content = models.CharField(max_length=280,default="Not Available Now",null=True)
    url = models.URLField(default="")
    author = models.CharField(max_length=50, default="Unknown", null=True)

    def __str__(self):
        return self.title


class Newscountrywise(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, default="")
    image = models.URLField(null=True, blank=True, default="")
    publishedAt = models.DateField(blank=True, null=True, default="datetime.date.today()")
    country = models.CharField(max_length=100,default="")
    description = models.CharField(max_length=280, default="Not Available Now",null=True)
    content = models.CharField(max_length=280,default="Not Available Now",null=True)
    url = models.URLField(default="")
    author = models.CharField(max_length=50, default="Unknown",null=True)

    def __str__(self):
        return self.title
