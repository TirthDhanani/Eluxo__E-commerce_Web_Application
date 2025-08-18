from django.shortcuts import render

# Create your views here.
def load_admin_login(request):
    return render(request,'admin/auth/login.html')