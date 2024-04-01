from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=False,null=False)
    phone_number = models.CharField(max_length=15)
    regarding = models.CharField(max_length=200)

    class Meta:
        db_table="user"