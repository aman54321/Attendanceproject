from django.shortcuts import render, redirect
from .models import Employee_Attendance
from django.contrib.auth import authenticate, login
from django.contrib import messages
from datetime import datetime
from django.http import HttpResponse
# Create your views here.

# def Employee_list(request):
#     employee = Employee_Attendance.objects.all()
#     if request.method == 'POST':
#         datef = request.POST['fromdate']
#         print(datef)
#         datet = request.POST['todate']
#         print(datet)
#         try:
#             employee=Employee_Attendance.objects.filter(date__lte=datet, date__gte=datef)
#             print(employee)
#         except:
#             employee=None
#         return render(request,'testdb/index.html', {'employee': employee})
#     print(employee)    
    
#     return render(request,'testdb/index.html', {'employee': employee})

def Employee_list(request):
    employee = Employee_Attendance.objects.all()
    if request.method == 'POST':
        datef = request.POST['fromdate']
        print(datef)
        datet = request.POST['todate']
        print(datet)
        try:
            t=Employee_Attendance.objects.filter(date__lte=datet, date__gte=datef)
            print(t)
        except:
            t=None
        return render(request,'testdb/data.html', {'t': t})
    print(employee)    
    
    return render(request,'testdb/home.html', {'employee': employee})
    


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print(user)
            login(request, user)
            messages.info(request,f"you are logged in as {username}")
            return redirect('Employee_list')
        else:
            messages.error(request,"Invalid username or password")
    return render(request, 'testdb/login.html')

# def date_query(request):
#     if request.method == 'POST':
#         start_date = request.POST.get('fromdate')
#         print(start_date)
#         end_date = request.POST.get('todate')
#         print(end_date)
#         employee = Employee_Attendance.objects.filter(date__range=[start_date,end_date])
#         print(employee)
#         return render(request, 'testdb/home.html', {'employee': employee})



# def name_query(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         data = Employee_Attendance.objects.filter(name='name')
#         return render(request, 'testdb/home.html',{'data': data})

import csv  
def exportcsv(request):
    students = Employee_Attendance.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=attendance.csv'
    writer = csv.writer(response)
    writer.writerow(['emp_id', 'name', 'date', 'check_in', 'check_out'])
    studs = students.values_list('emp_id','name', 'date', 'check_in', 'check_out')
    for std in studs:
        writer.writerow(std)
    return response


