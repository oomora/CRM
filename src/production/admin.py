from django.contrib import admin


from models import Activity
from forms import ActivityForm

# Register your models here.
class AdminActivities(admin.ModelAdmin):
    list_display =["activityName", "activityStandardTime", "activityTime", "step", "assignedTo", "assignedOrder"]
    search_fields = ('activityName', 'assignedTo')
    form = ActivityForm

admin.site.register(Activity, AdminActivities)

