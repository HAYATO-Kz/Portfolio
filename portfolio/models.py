from django.db import models

class Profile(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    contact = models.JSONField()

class Education(models.Model):
    start_year = models.CharField(max_length=7,default='Present')
    end_year = models.CharField(max_length=7,default='Present')
    department = models.CharField(max_length=30)
    university = models.CharField(max_length=30)

class Project(models.Model):
    title = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    github_link = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

class Experince(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')

class Skill(models.Model):
    SKILL_CHOICES = (
        ('1', 'Programming Language'),
        ('2', 'Frontend'),
        ('3', 'Backend'),
        ('4', 'Database'),
        ('5', 'Tool'),
        ('6', 'Other'),
    )
    type = models.CharField(max_length=1,choices=SKILL_CHOICES)
    title = models.CharField(max_length=30)

    def getText (self) :
        switcher = {
            "1": "Programming Language",
            "2": "Frontend",
            "3": "Backend",
            "4": "Database",
            "5": "Tool",
            "6": "Other",
        }
        return switcher.get(self.type)

class Inbox(models.Model):
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50,default='contact me')
    message = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)