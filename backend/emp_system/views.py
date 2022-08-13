from django.shortcuts import render
from .models import Employee,Role
from datetime import datetime
# Create your views here.
def index(request):
    return render(request,'index.html')


def view_emp(request):
    
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,'view_emp.html',context)
    print(context)

def add_emp(request):
    if request.method =='POST':
        first_name=request.POST('first_name')
        last_name=request.POST('last_name')
        salary=request.POST('salary')
        bonus=request.POST('bonus')
        phone=request.POST('phone')
        dept=request.POST('dept')
        role=request.POST('role')
        new_emp=Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,dept_id=dept,role_id=role,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse('Employee added Successfully')
    elif request.method=='GET':
        return render(request,'add_emp.html')
    else:
        return HttpResponse('Exception occurs')



def delete_emp(request):
    return render(request,'delete_emp.html')


def filter_emp(request):
    return render(request,'filter_emp.html')
