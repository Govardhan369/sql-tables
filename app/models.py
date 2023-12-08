from django.db import models
class Dept(models.Model):
    DeptNo=models.IntegerField(primary_key=True)
    DName=models.CharField(max_length=100)
    Loc=models.CharField(max_length=100)
class Employee(models.Model):
    Empno=models.IntegerField(primary_key=True)
    Ename=models.CharField(max_length=100)
    Job=models.CharField(max_length=100)
    MGR=models.IntegerField()
    HireDate=models.DateField()
    Salary=models.IntegerField()
    Comm=models.IntegerField()
    DeptNo=models.ForeignKey(Dept,on_delete=models.CASCADE)
class Salgrade(models.Model):
    Grade=models.CharField(max_length=100)
    Lsal=models.IntegerField()
    Hsal=models.IntegerField()
class Bonus(models.Model):
    Ename=models.CharField(max_length=100)
    Job=models.CharField(max_length=100)
    Salary=models.IntegerField()
    Comm=models.IntegerField()


# Create your models here.
