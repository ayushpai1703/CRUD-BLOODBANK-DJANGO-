# exe/views.py

from django.shortcuts import render

def handler404(request, exception):
    return render(request, 'error.html', {'exception': exception}, status=404)