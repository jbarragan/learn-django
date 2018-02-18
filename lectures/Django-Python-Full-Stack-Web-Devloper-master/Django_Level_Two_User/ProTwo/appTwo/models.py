from django.db import models

class User(models.Model):
    """docstring for User."""
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
