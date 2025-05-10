from django.db import models


class UsersModel(models.Model):
    id = models.IntegerField(db_index=True, primary_key=True, unique=True)
    mail = models.CharField(max_length=100, unique=True)
    psw = models.CharField(max_length=50)
    login = models.CharField(max_length=50, unique=True)
