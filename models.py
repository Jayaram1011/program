from django.contrib.auth.models import User
from django.db import models


class loginhistory(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    login_date_time = models.DateTimeField()