from django.shortcuts import render
from .models import storyModel
# Create your views here.
def base(request):
    context = {
        'base': base
    }
    return render(request, "base.html", context)
