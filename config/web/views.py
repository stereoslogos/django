from django.shortcuts import render

# Create your views here.
# Each view is a py function
def Home(request):
    return render(request, 'index.html')