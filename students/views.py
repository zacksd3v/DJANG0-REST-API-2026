from django.shortcuts import render
from django.http import HttpResponse

def students(request):
    students = [{
        'id': 1,
        'name': 'Mubarak Aliyu',
        'phone': 2348144773839
    }]
    return HttpResponse(students)