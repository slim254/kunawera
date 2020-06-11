from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Job(models.Model):
    job_id=models.IntegerField(primary_key=True)
    job_title=models.CharField(max_length=255)
    description=models.TextField(max_length=3000)
    salary=models.IntegerField()
    location=models.CharField(max_length=100)
    contact_phone=models.IntegerField()
    date_posted=models.DateTimeField(auto_now_add=True)
    employer=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
     return self.job_title


