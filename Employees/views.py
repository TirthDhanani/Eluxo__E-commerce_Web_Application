from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def load_employees(request):
    return render(request, 'employees.html')
def load_salaryslip(request):
    name = request.POST.get("name")
    salary = request.POST.get("salary")
    hra = int(salary)*2/100
    oa = int(salary)*3/100
    pf = int(salary)*14/100
    netsalary = int(salary)+hra+oa-pf
    netsalary1 = str(netsalary)
    context={
        "name" : name,
        "salary" : salary,
        "hra" : hra,
        "oa" : oa,
        "pf" : pf,
        "netsalary" : netsalary1
    }
    return render(request,'employees.html', context)


