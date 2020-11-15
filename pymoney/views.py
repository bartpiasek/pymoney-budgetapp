from django.shortcuts import render
from .models import *


# Create your views here.
def project_list(request):
    """
    docstring
    """
    return render(request, 'pymoney/main.html')