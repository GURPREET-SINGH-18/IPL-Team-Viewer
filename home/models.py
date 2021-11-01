from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BaseUser(User):
    address = models.CharField(max_length=50)
    mobile = models.CharField(max_length=12)
    date = models.DateField(auto_now_add=True)
    gender = models.CharField(max_length=10)
    
class addteam(models.Model):
    teamname = models.CharField(max_length=25)
    player=models.TextField(max_length=600)
    batsmen=models.CharField(max_length=2)
    bowler=models.CharField(max_length=2)
    wk=models.CharField(max_length=2)
    coach=models.CharField(max_length=40)
    img=models.ImageField(upload_to='pics')
    def __str__(self):
        return self.teamname