from django.db import models

class User(models.Model):
    """docstring for User"""
    user_email = models.EmailField(primary_key=True)
    user_first_name = models.CharField(max_length=30)
    user_last_name = models.CharField(max_length=30)
    user_middle_name = models.CharField(max_length=30, blank=True)
    user_address = models.CharField(max_length=100)
    user_address_optional = models.CharField(max_length=100, blank=True)
    tel_number = models.CharField(max_length=20)
    website = models.CharField(max_length=45, blank=True)

class Settings(models.Model):
    """docstring for Settings"""
    passcode = models.CharField(max_length=45)
    theme = models.CharField(max_length=45)
    user = models.ForeignKey(User)

class Award(models.Model):
    """docstring for Award"""
    award_name = models.CharField(max_length=45)
    time = models.DateField()
    description = models.TextField(blank=True)
    user = models.ForeignKey(User)

class Work(models.Model):
    """docstring for Work"""
    company_name = models.CharField(max_length=60)
    job_title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    company_url = models.CharField(max_length=45)
    start_time = models.DateField()
    end_time = models.DateField()
    location = models.CharField(max_length=100)
    achievement = models.TextField(blank=True)
    visible = models.BooleanField()
    user = models.ForeignKey(User)
