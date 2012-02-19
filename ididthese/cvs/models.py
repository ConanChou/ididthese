from django.db import models
import datetime

class User(models.Model):
    """docstring for User"""
    user_email = models.EmailField(primary_key=True)
    user_first_name = models.CharField(max_length=30)
    user_last_name = models.CharField(max_length=30)
    user_middle_name = models.CharField(max_length=30, blank=True)
    user_address = models.CharField(max_length=100)
    user_address_optional = models.CharField(max_length=100, blank=True)
    user_city = models.CharField(max_length=20)
    user_state = models.CharField(max_length=2)
    user_zip = models.CharField(max_length=10)
    tel_number = models.CharField(max_length=20)
    website = models.CharField(max_length=45, blank=True)


class Settings(models.Model):
    """docstring for Settings"""
    passcode = models.CharField(max_length=45)
    theme = models.CharField(max_length=45)
    user = models.ForeignKey(User)


class Tag(models.Model):
    """docstring for tag"""
    tag_name = models.CharField(max_length=45)


class Achievement(models.Model):
    description = models.TextField(blank=True)


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    is_pet = models.BooleanField()
    description = models.TextField(blank=True)
    role = models.CharField(max_length=100,blank=True)
    url = models.TextField(blank=True)
    time = models.DateField('finish time')
    tags = models.ManyToManyField(Tag)
    skills = models.ManyToManyField('Skill')


class Award(models.Model):
    """docstring for Award"""
    award_name = models.CharField(max_length=45)
    time = models.DateField()
    description = models.TextField(blank=True)
    user = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag)


class Work(models.Model):
    """docstring for Work"""
    company_name = models.CharField(max_length=60)
    job_title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    company_url = models.CharField(max_length=45,blank=True)
    start_time = models.DateField()
    end_time = models.DateField()
    location = models.CharField(max_length=100)
    achievement = models.ForeignKey(Achievement,blank=True)
    visible = models.BooleanField()
    user = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag)
    projects = models.ForeignKey(Project)


class School(models.Model):
    school_id = models.AutoField(primary_key=True)
    school_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    first_major = models.CharField(max_length=100)
    second_major = models.CharField(max_length=100, blank=True)
    minor_major = models.CharField(max_length=100, blank=True)
    start_time = models.DateField('period start date')
    end_time = models.DateField('period end date')
    location = models.CharField(max_length=100)
    gpa_general = models.DecimalField(max_digits=2,decimal_places=1)
    gpa_visible = models.BooleanField()
    gpa_profession = models.DecimalField(max_digits=2,decimal_places=1,blank=True)
    gpa_profession_visible = models.BooleanField()
    visible = models.BooleanField()
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.school_name
    def was_published_today(self):
        return self.start_time.date() == datetime.date.today()


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    school = models.ForeignKey(School)
    description = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag)
    projects = models.ForeignKey(Project)
    visible = models.BooleanField()


class Skill(models.Model):
    skill_name = models.CharField(max_length=50)
    skill_level = models.IntegerField()
    visable = models.BooleanField()
    user = models.ForeignKey(User)
    catagory = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag)


