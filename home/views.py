"""
Home page app views
"""
from django.shortcuts import render


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


# def homepage_view(request):
#     """ A view used to test 500 error page """

#     raise Exception("This is a test error")
