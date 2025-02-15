from django.db import models
class Departments(models.Model):
    dept_name=models.CharField(max_length=100)
    dept_description=models.TextField()
    def __str__(self):
        return self.dept_name
class Doctors(models.Model):
    doc_name=models.CharField(max_length=255)
    doc_spec=models.CharField(max_length=255)
    dept_name=models.ForeignKey(Departments,on_delete=models.CASCADE)
    doc_image=models.ImageField(upload_to='doctors')


