from django.db import models

# Create your models here.


class Citation(models.Model):
    street = models.CharField(max_length=15)
    date = models.DateTimeField()
    officer = models.CharField(max_length=15)





