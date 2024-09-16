from django.shortcuts import render
from django.http import HttpResponse
from employees.models import Employee
# from . import forms

def home(request):
  data = Employee.objects.all()
  total_employees = data.count()
  context = {
    "data" : data,
     "total_employees" : total_employees,
  }
  return render(request, 'home.html', context=context)
