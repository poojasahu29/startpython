from django.db import models
# Create your models here.

class employee(models.Model):#here Model is database class to inherited by models packages
	fname=models.CharField(max_length=200)
	mname=models.CharField(max_length=200, default='-')
	lname=models.CharField(max_length=200)
	age=models.IntegerField(default=0)
	email=models.CharField(max_length=200)
	mobile=models.IntegerField(default=0)

	def __str__(self):
		return self.fname
class details(models.Model):
	e=models.ForeignKey(employee, on_delete=models.CASCADE,default=0)
	address= models.TextField(default=0)
	'''pincode=models.IntegerField(default=0)
	city=models.TextField(default=0)'''
