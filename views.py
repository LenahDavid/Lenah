from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .models import table,business
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login
from rest_framework import viewsets
from .serializers import TableSerializers
from django.core.mail import send_mail
import math,random
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

class TableViewSet(viewsets.ModelViewSet):
    queryset = table.objects.all()
    serializer_class=TableSerializers

def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

def send_otp(request):
    Email=request.POST.get("Email")
    o=generateOTP()
    htmlgen = '<p>Your OTP is <strong>+0+</strong></p>'
    send_mail('OTP request',o,'<gmail id>',[Email],fail_silently=False,html_message=htmlgen)
    return HttpResponse(o)

def login(request):
    if request.method == 'POST':
        Email = request.POST.get('email')                   
        Password = request.POST.get('password')

        user = auth,authenticate(request,Email=Email, Password=Password)

        if user is not None:
            messages.success(request, f' wecome {Email} !!')
            return redirect('about-us.html')
        else:
            messages.info(request,'invalid credentials')
            return redirect('signup.html')
    else:
        return render(request, 'login.html')

def signup(request):
     if request.method == 'POST':
         Firstname = request.POST['first-name']
         Lastname = request.POST['last-name']
         surname = request.POST['surname']
         Email = request.POST['email']
         Phone_number = request.POST['phone-number']
         Age = request.POST['age']
         Gender = request.POST['gender']
         nationality = request.POST['nationality']
         City = request.POST['city']
         country = request.POST['country']
         address1 = request.POST['address1']
         Address2 = request.POST['address2']
         PostalCode = request.POST['postal-code']
         Password = request.POST['create-password']
         confirmPassword = request.POST['confirm-password']

         if Password == confirmPassword:
            if table.objects.filter(Email=Email).exists():
                messages.info(request,'Email already used')
                return redirect('signup.html')

            elif table.objects.filter(Phone_number=Phone_number).exists():
                messages.info(request,'phonenumber already exists')
                return redirect('signup.html')
            else:
                user=table.objects.create(Firstname=Firstname, Lastname=Lastname, surname=surname, Email=Email,Phone_number=Phone_number,Age=Age, Gender=Gender,nationality=nationality, City=City,country=country,address1=address1,Address2=Address2,PostalCode=PostalCode,Password=Password)
                user.save()
                return redirect('dashboard.html')
         else:
            messages.info(request,'password is not the same')
            return redirect('signup.html')
     else:
        return render(request, 'signup.html')

def logout(request):
    authenticate.logout(request)
    return redirect('about-us.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def aboutus(request):
    return render(request, 'about-us.html')

def businessregform(request):
    if request.method == 'POST':
         business_name = request.POST['business name']
         contact_number = request.POST['contact number']
         email = request.POST['email']
         country = request.POST['Country']
         street_address = request.POST['Street Address']
         streetaddress2 = request.POST['Street address 2']
         city = request.POST['city']
         region = request.POST['Region']
         postalcode = request.POST['Postal/Zip code']
         password = request.POST['password']
         confirmpassword = request.POST['confirm password']

         if password == confirmpassword:
            if business.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return redirect('business reg form.html')
            elif business.objects.filter(contact_number=contact_number).exists():
                messages.info(request,'phonenumber already exists')
                return redirect('business reg form.html')
            else:
                user=business.objects.create(business_name=business_name, contact_number=contact_number, email=email, region=region,postalcode=postalcode, city=city,country=country,street_address=street_address,streetaddress2=streetaddress2,password=password)
                user.save()
                return redirect('dashboard.html')
         else:
            messages.info(request,'password is not the same')
            return redirect('business reg form.html')
    else:
        return render(request, 'business reg form.html')


    

def choose_wallet(request):
    return render(request, 'choosewallet.html')

def client_profile(request):
    return render(request, 'client_profile.html')

def client_update_profile(request):
    return render(request, 'client_update_profile.html')

def client_update(request):
    return render(request, 'client_update.html')

def demo(request):
    return render(request, 'demo.html')

def faqs(request):
    return render(request, 'faqs.html')

def features(request):
    return render(request, 'features.html')

def forgot_password(request):
    return render(request, 'forgot_password.html')

def helpcenter(request):
    return render(request, 'helpcenter.html')

def HELPLINE(request):
    return render(request, 'HELPLINE.html')

def history(request):
    return render(request, 'history.html')

def index(request):
    return render(request, 'index.html')

def nav(request):
    return render(request, 'nav.html')

def pay(request):
    return render(request, 'pay.html')

def rateus(request):
    return render(request, 'rateus.html')

def remove_wallet(request):
    return render(request, 'removewallet.html')

def services(request):
    return render(request, 'services.html')

def shop_ver_page(request):
    return render(request, 'shop varification page.html')

def side(request):
    return render(request, 'side.html')

def transaction(request):
    return render(request, 'transaction.html')

def update_shop_profile(request):
    return render(request, 'update shop profile.html')

def verification_page(request):
    return render(request, 'verification_page.html')

def add_wallet(request):
    return render(request, 'add-wallet.html')

def shopvarificationpage(request):
    return render(request, 'shopvarificationpage')

@api_view(['GET','POST'])
def table_list(request, format=None):

     if request.method == 'GET':
      tables = table.objects.all()
      serializers = TableSerializers(tables, many=True)
      return JsonResponse(serializers.data, safe=False)


     if request.method =='POST':

        serializer = TableSerializers(data=request.data)
        if serializer.is_valid():
           
             serializer.save()
             return Response(serializer.data,status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def table_list2(request, id, format=None):
    try:
        tables = table.objects.get(pk=id)
    except table.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method =='GET':
        serializer = TableSerializers(tables)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TableSerializers(tables, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        tables.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

         
    
    
    



    

    
    
