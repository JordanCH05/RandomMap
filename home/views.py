from django.shortcuts import render
from .forms import MapForm


def index(request):
    """ A view to return the index page """
    form = MapForm()

    context = {
        'form': form
    }

    return render(request, 'home/index.html', context)
