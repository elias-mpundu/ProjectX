from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def image_viewer(request):
    template = loader.get_template('image_viewer.html')
    return HttpResponse(template.render())