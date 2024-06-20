from django.db import models

# Create your models here.
class Donations(models.Model):
    amount = models.IntegerField
    name = models.CharField(max_length=128)
    accNo = models.IntegerField
    reference = models.CharField(max_length=128,null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    donation_made = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Message(models.Model):
    #user = 
    donations = models.ForeignKey(Donations, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    donation_made = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[0:50]