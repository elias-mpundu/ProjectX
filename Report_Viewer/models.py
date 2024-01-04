from django.db import models
from Users.models import toolboxUser
# Create your models here.
# Create your models here.

class Patient(models.Model):
    firstName = models.CharField(max_length = 100, blank = True, null = True)
    lastName = models.CharField(max_length = 100, blank = True, null = True)
    mrn = models.IntegerField(blank = True, null = True)
    dateOfBirth = models.DateField(auto_now=False, auto_now_add=False, blank = True, null = True)
    researcher = models.ForeignKey(toolboxUser, on_delete=models.CASCADE, default = 1, related_name = "patient")

    
    class Meta:
        verbose_name_plural="Patients"

    def __str__(self):
        return self.lastName
        #change to a unique identifier later

class Visit(models.Model):
    visitID = models.CharField(max_length = 100, blank = True, null = True)
    visitCount = models.IntegerField(blank = True, null = True)
    visitDate = models.DateField(auto_now=False, auto_now_add=False, blank = True, null = True)
    patientNumber = models.ForeignKey(Patient, on_delete=models.CASCADE, default = 1, related_name = "visit")

    
    class Meta:
        verbose_name_plural="Visits"

    def __str__(self):
        return self.visitID
        #change to a unique identifier later

class ImageData(models.Model):
    imageDataID = models.CharField(max_length = 100, blank = True, null = True)
    whichEye = models.CharField(max_length = 100, blank = True, null = True)
    fullImage = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank = True, null = True)
    retinalImage = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank = True, null = True)
    thicknessImage = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank = True, null = True)
    enfaceImage = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank = True, null = True)
    visitNumber = models.ForeignKey(Visit, on_delete=models.CASCADE, default = 1, related_name = "imagedata")

    
    class Meta:
        verbose_name_plural="Image Data"

    def __str__(self):
        return self.imageDataID
        #change to a unique identifier later

class ReportData(models.Model):
    reportDataID = models.CharField(max_length = 100, blank = True, null = True)
    reportImage = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank = True, null = True)
    visitNumber = models.ForeignKey(Visit, on_delete=models.CASCADE, default = 1, related_name = "reportdata")

    
    class Meta:
        verbose_name_plural="Report Data"

    def __str__(self):
        return self.reportDataID
        #change to a unique identifier later
