from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee
from . import forms

def add_employee(request):
    if request.method == 'POST':
        employee_form = forms.EmployeeForm(request.POST)
        if employee_form.is_valid():
            employee_form.save()
            return redirect('add_employee')
        else:
            return render(request, 'add_employees.html', {'form': employee_form})
    else:
        employee_form = forms.EmployeeForm()    
        return render(request, 'add_employees.html', {'form': employee_form})
  

def update_employee(request, id):
    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return HttpResponse("Employee not found")

    if request.method == 'POST':
        employee_form = forms.EmployeeForm(request.POST, instance=employee)
        if employee_form.is_valid():
            employee_form.save()
            return redirect('edit_employee')
    else:
        employee_form = forms.EmployeeForm(instance=employee)
    
    return render(request, 'update_employee.html', {'form': employee_form})

def delete_employee(request, id):
    try:
        employee = Employee.objects.get(id=id)
        employee.delete()
        return redirect('edit_employee')
    except Employee.DoesNotExist:
        return HttpResponse("Employee not found")


def home(request):
  data = Employee.objects.all()
  return render(request, 'edit_employees.html', {'data': data})

def view_profile(request, id):
    try:
        data = Employee.objects.get(id=id)
        return render(request, 'view_profile.html', {'data': data})
    except Employee.DoesNotExist:
        return HttpResponse("<h1>Employee not found</h1>")

