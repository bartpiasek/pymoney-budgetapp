from django.shortcuts import render

# Create your views here.
def project_list(request):
    """
    docstring
    """
    return render(request, 'mymoney')