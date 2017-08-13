from django.shortcuts import render
from django.template.loader import render_to_string

from .models import Waypoint


# Create your views here.

def index(response):
    waypoints = Waypoint.objects.order_by('name')
    """return render(response, 'PrimerMapa/index.html', {
        'waypoints': waypoints,
        'content': render_to_string('PrimerMapa/waypoints.html', {
            'waypoints': waypoints
        })
    })"""
    return render(response, 'PrimerMapa/index.html', {})
