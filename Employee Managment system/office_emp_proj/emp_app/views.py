from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from datetime import datetime
from django.db.models import Q

# Create your views here.
def  index(request):
    return render(request, 'emp_app/index.html')

def  all_emp(request):
    emps = Employee.objects.all()
    context = {'emps':emps}
    return render(request, 'emp_app/all_emp.html' , context)

def  add_emp(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = request.POST['dept']
        salary = request.POST['salary']
        hours = request.POST['hours']
        role = request.POST['role']
        phone = request.POST['phone']
        
        new_emp = Employee(first_name = first_name, last_name = last_name , dept_id = dept, salary = salary, hours = hours, role_id = role, phone = phone, hire_date=datetime.now())
        new_emp.save()
        return render(request, 'emp_app/index.html')


    return render(request, 'emp_app/add_emp.html')

def  remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse('Employee Removed')
        except:
            return HttpResponse("Employee not exist")

    emps = Employee.objects.all()
    context = {'emps':emps}
    return render(request, 'emp_app/remove_emp.html', context)

def  filter_emp(request):
    if request.method=='POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(first_name__icontains=name))

        if dept:
            emps = emps.filter(dept__name__icontains=dept)

        if role:
            emps = emps.filter(role__name__icontains=role)

        context ={
            'emps':emps
        }
        return render(request, 'emp_app/all_emp.html', context = context)
    return render(request, 'emp_app/filter_emp.html')