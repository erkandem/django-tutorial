from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """simplest view in django?"""
    return HttpResponse(
        "Hello, world! You're at the `my_app` index page"
    )
