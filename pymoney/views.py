from django.shortcuts import get_object_or_404, render
from .models import *


# Create your views here.
def project_list(request):
    """
    """
    return render(request, 'pymoney/main_list.html')


def project_details(request, project_slug):
    """
    """
    budget = get_object_or_404(Budget, slug=project_slug)
    return render(request, 'pymoney/main_details.html', {'budget':budget})