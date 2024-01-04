from django.contrib import admin
from .models import toolboxUser
from Report_Viewer.models import Patient
from Report_Viewer.models import Visit
from Report_Viewer.models import ImageData
from Report_Viewer.models import ReportData
#from toolbox.models import Patients, RiskFactor, FamilyHistory, IOPSurgeries, Visit, ScannedInputPatients, ScannedInputVisits, AppRiskFactor, AppFamilyHistory, ScannedAppPatient, ScannedAppVisit, AppIOPSurgeries, ScannedOCT_Disc_AppVisit, ScannedOCT_Gang_AppVisit
# Register your models here.
class toolboxUserAdmin(admin.ModelAdmin):
    pass
#registers models
admin.site.register(toolboxUser, toolboxUserAdmin)
admin.site.register(Patient)
admin.site.register(Visit)
admin.site.register(ImageData)
admin.site.register(ReportData)