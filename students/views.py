from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def load_result(request):

    
    
    return render(request, 'result.html',)
def add_avg(request):
    rollno = request.POST.get("rollno")
    name = request.POST.get("name")
    gujarati = request.POST.get("guj")
    english = request.POST.get("eng")
    hindi = request.POST.get("hin")
    total = int(gujarati)+ int(english) +int (hindi)
    avg= total/3
    student_result = {

        "rollno" : rollno,
        "name" : name,
        "gujarati" : gujarati,
        "english" : english,
        "hindi" : hindi,
        "total" : total,
        "avg" : avg
    }
    return render(request, 'result.html',student_result)

    

