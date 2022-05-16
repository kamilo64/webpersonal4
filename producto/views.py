from django.shortcuts import render
from .models import Project

def producto(request):
    projects=Project.objects.all()
    return render(request,"producto/producto.html",{'projects':projects})