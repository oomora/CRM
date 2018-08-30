from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Activity(models.Model):
    class Meta:
        verbose_name_plural='Activities'
    activityName        = models.CharField(max_length=120,blank=True,null=True)
    activityStandardTime= models.IntegerField(default=0)
    activityTime        = models.IntegerField(default=0)
    step                = models.IntegerField(default=10)
    assignedTo          = models.CharField(max_length=30,blank=True,null=True)
    assignedOrder       = models.CharField(max_length=30,blank=True,null=True)

    def __unicode__(self):
        return self.activityName

    def __str__(self):
        return self.activityName

class ProcessRoute(models.Model):
    repairActivities = models.ManyToManyField(Activity)
    assignedToPR = models.CharField(max_length=30, blank=True, null=True)

    def __unicode__(self):
        return self.processRouteId

    def __str__(self):
        return self.processRouteId

class Bom(models.Model):
    repairRoute = models.ManyToManyField(ProcessRoute)
    workOrder   = models.CharField(max_length=25, blank=True, null=False)
    workTime    = models.IntegerField(default=0)

class Employee(models.Model):
    name = models.CharField(max_length=80, blank=True, null= True)
    lastName = models.CharField(max_length=80, blank=True, null= True)
    employeeNumber = models.IntegerField(default=0)
    salary = models.IntegerField(default=0)
    admission = models.DateField()
