__author__ = 'oscarmora'
from django import forms

from models import *

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ["activityName", "activityStandardTime","activityTime","step","assignedTo", "assignedOrder"]
        labels ={
            'activityName': 'Actividad',
            'activityStandardTime': 'Tiempo Estandard',
            'activityTime': 'Esfuerzo Actividad',
            'step': 'Paso',
            'assignedTo': 'Asignada a',
            'assignedOrder': 'Orden',
        }

class ProcessRouteForm(forms.ModelForm):
    class Meta:
        model = ProcessRoute
        fields = ["repairActivities", "assignedToPR"]

class BomForm(forms.ModelForm):
    class Meta:
        model = Bom
        fields = ["repairRoute", "workOrder","workTime"]

    repairRoute = models.ManyToManyField(ProcessRoute)
    workOrder   = models.CharField(max_length=25, blank=True, null=False)
    workTime    = models.IntegerField(default=0)