from django.db import models
class Departments(models.Model):
    dept_name=models.CharField(max_length=100)
    dept_description=models.TextField()

