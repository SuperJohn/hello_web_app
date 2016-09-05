from django.shortcuts import render

# create your new views here
def index(request):
    # this is your new view
    return render(request, 'index.html')