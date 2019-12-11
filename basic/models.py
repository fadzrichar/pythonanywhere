import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class Blog(models.Model):
    image_path = models.CharField(max_length=255, default = None, blank = True)
    blog_title = models.CharField(max_length=255, default = None, blank = True)
    blog_content = models.TextField(max_length=2000, default = None, blank = True)
    pub_date = models.DateField('date published', auto_now_add = True)

    def __str__(self):
        return self.blog_title

class Mentor(models.Model):
    image_path = models.CharField(max_length=255)
    mentor_name = models.CharField(max_length=255)
    mentor_exp = models.CharField(max_length=255)
    mentor_testi = models.CharField(max_length=255)

    def __str__(self):
        return self.mentor_name

class Mentee(models.Model):
    image_path = models.CharField(max_length=255)
    mentee_name = models.CharField(max_length=255)
    mentee_testi = models.CharField(max_length=255)

    def __str__(self):
        return self.mentee_name