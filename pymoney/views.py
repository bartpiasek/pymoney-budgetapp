from django.shortcuts import render
from .models import *


# Create your views here.
def project_list(request):
    """
    """
    return render(request, 'pymoney/main_list.html')


def project_details(request, project_slug):
    """
    """
    return render(request, 'pymoney/main_details.html')