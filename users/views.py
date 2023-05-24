from django.shortcuts import render
from django.http import HttpResponse

def WhoamiView(request):
    role=None
    if request.user:
        role = request.user.role
    html = "<html><body>You role is %s.</body></html>" % role
    return HttpResponse(html)
