from django.db import models
import datetime

# Create your models here.
class School(models.Model):
    school_id = models.AutoField(primary_key=True)
    school_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    start_time = models.DateField('period start date')
    end_time = models.DateField('period end date')
    location = models.CharField(max_length=100)
    gpa_general = models.DecimalField(max_digits=2,decima_places=1)
    gpa_profession = models.DecimalField(max_digits=2,decima_places=1,blank=True)
    visible = models.BooleanField()
    user = models.ForeignKey(User)
    
    
    def __unicode__(self):
        return self.school_name
    def was_published_today(self):
        return self.start_time.date() == datetime.date.today()
        

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    school = models.Foreignkey(School)
    description = models.TextField(blank=True)
    credits = models.IntegerField()
    visible = models.BooleanField()
    
class Skill(models.Model):
    skill_name = models.CharField(max_length=50)
    skill_level = models.IntegerField()
    visable = models.BooleanField()
    user = models.ForeignKey(User)
    catagory = models.CharField(max_length=50)
    
class Project(models.Model):
    project_name = models.CharField(max_length=100)
    is_pet = models.Boolean()
    description = models.TextField(blank=True)
    role = models.CharField(max_length=100,blank=True)
    url = models.TextField(blank=True)
    time = models.DateField('finish time')
    work = models.ForeignKey(Work)
    
    
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

class tag(models.Model):
    """docstring for tag"""
    tag_name = models.CharField(max_length=45)
    
    
    
    
    
    
    
    
    
    
    
    
    
