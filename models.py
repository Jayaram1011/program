from django.db import models


class Details(models.Model):
    username = models.CharField(max_length=100,null=False)
    password =models.CharField(max_length=100,null=False)

    
class History(models.Model):
    user_id = models.ForeignKey(Details,on_delete=models.CASCADE)
    timestamp = models.DateTimeField()