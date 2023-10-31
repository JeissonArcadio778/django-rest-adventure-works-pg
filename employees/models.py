from django.db import models

class Employee(models.Model):
    businessentityid = models.IntegerField(primary_key=True)
    nationalidnumber = models.CharField(max_length=15)
    loginid = models.CharField(max_length=256)
    jobtitle = models.CharField(max_length=50)
    birthdate = models.DateField()
    maritalstatus = models.CharField(max_length=1)
    gender = models.CharField(max_length=1)
    hiredate = models.DateField()
    salariedflag = models.BooleanField(default=True)
    vacationhours = models.SmallIntegerField(default=0)
    sickleavehours = models.SmallIntegerField(default=0)
    currentflag = models.BooleanField(default=True)
    rowguid = models.UUIDField()
    modifieddate = models.DateTimeField(auto_now=True)
    organizationnode = models.CharField(max_length=255, default='/')

    # class Meta:
    #     db_table = '"humanresources"."employee"'
    #     managed = False
