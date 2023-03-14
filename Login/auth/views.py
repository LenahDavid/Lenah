from base64 import urlsafe_b64decode, urlsafe_b64encode
from email.message import EmailMessage
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from Login import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from . tokens import TokenGenerator


def home(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        #username = request.POST.get('username')
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, 'Username already exists')
            return redirect('home')
        
        if User.objects.filter(email=email):
            messages.error(request,'Email already exists')
            return redirect('home')

        if len(username)>10:
            messages.error(request,'Username must be under 10 characters')

            if pass1 != pass2:
                messages.error(request,'Password does not match')

                if not username.isalnum():
                    messages.error(request,'Username must be alpha numeric')
                    return redirect('home')
                
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False
        myuser.save()

        messages.success(request,'Account Successfully created.Confirmation email sent')

        subject = 'Welcome to our website login'
        message = 'Hello' + myuser.first_name + 'Confirm email address'
        from_email =settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        current_site = get_current_site(request)
        email_subject = 'Confirm your email'
        message2 = render_to_string('email_confirmation.html',{

         'name': myuser.first_name,
         'domain': current_site.domain,
         'uid':urlsafe_b64encode(force_bytes(myuser.pk)),
         'token':TokenGenerator.make_token(myuser)
        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],

        )
        email.fail_silently = True
        email.send()

        return redirect('signin')

    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request,user)
            fname = user.first_name
            return render(request,'index.html', {'fname':fname})
        
        else:
            messages.error(request,'Bad Credentials')
            return redirect('home')
    return render(request, 'signin.html')

def signout(request):
 logout(request)
 messages.success(request, 'Logged out Successfully')
 return redirect('home')

def activate(request, uidb64, token):
 try:
        uid = force_text(urlsafe_b64decode(uidb64))
        myuser = User.objects.get(pk=uid)
 except (TypeError, ValueError, OverflowError, User.DoesNotExist):
       myuser = None

 if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active =True
        myuser.save()
        login(request,myuser)
        return redirect('home')
 else:
        return render(request, 'activation_failed.html')