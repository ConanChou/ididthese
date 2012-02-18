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
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    