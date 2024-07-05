from django.db import models
from .user import User

# Create your models here.
class Donation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    accNo = models.IntegerField()
    reference = models.CharField(max_length=128,null=True, blank=True)
    message = models.TextField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    

   
    
# class Message(models.Model):
#     #user = 
#     donations = models.ForeignKey(Donation, on_delete=models.CASCADE)
#     body = models.TextField()
#     updated = models.DateTimeField(auto_now=True)
#     donation_made = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.body[0:50]
    