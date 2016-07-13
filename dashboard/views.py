from django.shortcuts import render
from django.http import HttpResponse
from utils.view_functions import render_to


@render_to('dashboard/dashboard.html')
def index(request):
    pass


def dashboard(request, **kwargs):
    pass
