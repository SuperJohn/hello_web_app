from django.shortcuts import render

# create your new views here
def index(request):
    # defining the variable
    number = 6
    thing = "Super John"
    # this is your new view
    return render(request, 'index.html',
                  {'number' : number, 'thing':thing, }
                  )

