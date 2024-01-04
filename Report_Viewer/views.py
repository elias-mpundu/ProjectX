from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.files.storage import FileSystemStorage

# Create your views here.
def report_viewer(request):
    template = loader.get_template('report_viewer.html')
    return HttpResponse(template.render())

def profile(request):
    template = loader.get_template('profile.html')
    return HttpResponse(template.render())

if request.method == "POST":
    # if the post request has a file under the input name 'document', then save the file.
    request_file = request.FILES['document'] if 'document' in request.FILES else None
    if request_file:
            # save attached file
 
            # create a new instance of FileSystemStorage
            fs = FileSystemStorage()
            file = fs.save(request_file.name, request_file)
            # the fileurl variable now contains the url to the file. This can be used to serve the file when needed.
            fileurl = fs.url(file)
 
return render(request, "template.html")