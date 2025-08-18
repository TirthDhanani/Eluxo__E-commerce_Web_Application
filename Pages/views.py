from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from Cart.models import CartModel
from django.core.mail import send_mail
import secrets
# Create your views here.
def load_home(request):

    return render(request,'home.html')

def load_about(request):
    return render(request,'about.html')


def load_register(request):
    if request.method  == "GET":
        return render(request,'register.html')
    else:
        try:
            firstname = request.POST.get("firstname")
            lastname = request.POST.get("lastname")
            email = request.POST.get("email")
            password = request.POST.get("password")

            user = User.objects.create_user(email, email, password)
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            messages.success(request, "Register Successfully")
        except Exception as e:
            messages.error(request, "Email already exist!")
        return redirect('/register')

def checkout(request):
    cartdata = CartModel.objects.filter(user = request.user)
    subtotal = 0 
    for row in cartdata:
        subtotal += float(row.getproducttotal())
    disamt = 0
    disamt = float(request.session.get('disamt', 0))
    context ={
        'cartdata' : cartdata,
        'subtotal' : subtotal,
        'finaltotal' :subtotal - disamt,
        'disamt':disamt
    }
    
    return render(request, "checkout.html", context)
def checklogin(request):
    try:
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Email or password not found")
            return redirect('/register')
    except Exception as e:
        messages.error(request, "Email or password not found")
    return redirect('/register')
def load_forgot_password(request):
    if request.method == "GET":
        return render(request, 'forgotpassword.html')
    else:
        email = request.POST.get("email")
        if User.objects.filter(email = email).exists():
            otp = str(secrets.randbelow(10_000)).zfill(4)
            user =  User.objects.get(email = email)
            request.session['otp'] = otp
            request.session['id'] = user.id
            send_mail(
                subject="Hello from Django",
                message="Your OTP = " + otp,
                from_email="tirthdhanani0243@gmail.com",
                recipient_list=[email],
            )
            return redirect('/otp')
        else:
            return redirect('/forgotpassword')

        #EMAIL
        #tirthdhanani0243@gmail.com
        #ukvv hccq chgj ilqz


        #EMAIL

def checklogout(request):
    logout(request)
    return redirect('/register')
    
def otpverify(request):
    if request.method == 'GET':
        return render(request, "otp.html")
    else:
        otp = ''.join([request.POST['d1'], request.POST['d2'], request.POST['d3'], request.POST['d4']])
        sentotp = request.session['otp'] 
        if sentotp == otp:
            messages.success(request,'OTP verified successfully!')
            return redirect('/setnewpass')
        
        else:
            messages.success(request,'Incorrect OTP')
            return redirect('/otp')
    
def setnewpass(request):
    if request.method =='GET':
        return render(request, "setnewpass.html")
    else:
        newpass = request.POST.get('newpass')
        confirmpass = request.POST.get('confirmpass')

        user = User.objects.get(id = request.session['id'])
        user.set_password(newpass)
        user.save()
        return redirect('/register')
        

        
