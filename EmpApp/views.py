from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Create your views here.

def index(request):

    return render(request, 'EmpApp/index.html')


def all_emp(request):

    try:
        all_emp = Employee.objects.all()
    except Employee.DoesNotExist:
        all_emp = None

    context = {"all_emp":all_emp}

    return render(request, "EmpApp/all_emp.html", context)



def add_emp(request):
    try:
        all_dept = Department.objects.all()
        all_role = Role.objects.all()    
    except Employee.DoesNotExist:
        all_dept = []
        all_role = []

    if request.method == "POST":
        try:
            first_name = request.POST["firstName"]
            last_name = request.POST["lastName"]
            dept = int(request.POST["department"])
            role = int(request.POST["role"])
            salary = int(request.POST["salary"])
            bonus = int(request.POST["bonus"])
            phone = int(request.POST["phone"])
            hire_date = request.POST["hireDate"]

            new_emp = Employee(first_name=first_name, last_name=last_name, dept_id=dept, role_id=role, salary=salary, bonus=bonus, phone=phone, hire_date=hire_date)
            new_emp.save()
            messages.success(request, "Employee added successfully.")

        except Exception as e:

            messages.error(request, f"An error occurred: {e}")

    context = {"all_dept": all_dept, "all_role": all_role}

    return render(request, "EmpApp/add_emp.html", context)



def delete_emp(request, emp_id=0):
    if emp_id:
        emp_obj = get_object_or_404(Employee, id=emp_id)

        try:
            emp_obj.delete()
            messages.success(request, "Employee deleted successfully.")

        except Exception as e:
            messages.error(request, f"An error occurred: {e}")

    return render(request, "EmpApp/delete_emp.html")


def filter_emp(request):
    if request.method == "POST":
        name = request.POST["name"]
        dept = request.POST["dept"]
        role = request.POST["role"]

        emps = Employee.objects.all()

        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))

        if dept:
            emps = emps.filter(dept__name__icontains=dept)

        if role:
            emps = emps.filter(role__name__icontains=role)

        context = {"all_emp": emps}

        return render(request, "EmpApp/all_emp.html", context)
    else:
        return render(request, "EmpApp/filter_emp.html")