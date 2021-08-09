from django.contrib.auth.models import User
from django.contrib import auth
from validate_email import validate_email
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.urls import reverse
from .utils import tokenGen
import json

# Create your views here.
class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')
    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        context = {
            'fieldValues': request.POST
        }

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if len(password) < 6:
                    print(password)
                    messages.error(request, 'Password too short')
                    return render(request, 'authentication/register.html', context)

                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.is_active = False
                user.save()
                uidb64 = urlsafe_base64_encode(force_bytes(User.pk))
                current_site = get_current_site(request)
                link = reverse('activate', kwargs={
                    'uidb64' : uidb64, 'token' : tokenGen.make_token(user)
                })
                verificationLink = 'http://'+ current_site.domain + link

                message = f'Hi {user.username}, Please the link below to activate your account \n {verificationLink}'
                mail_subject = 'An email'
                email = EmailMessage(
                            mail_subject, message, to=[email]
                )
                email.send(fail_silently=False)
                messages.success(request, 'Account created successfully')
                print(user)
                return render(request, 'authentication/register.html')
        return render(request, 'authentication/register.html')


class UsernameAuthentication(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error' : 'username should only contain alnumeric characters'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error' : 'username is not available'},status=400)
        return JsonResponse({'username_valid' : True})

class EmailAuthentication(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error' : 'invalid email'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error' : 'email id already exist'}, status=400)
        return JsonResponse({'email_valid' : True})

class verification(View):
    def get(self, request, uidb64, token):
        
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.filter(pk=uidb64)
            
            if not tokenGen.check_token(user, token):
                return redirect('login'+'message'+'Account already activated')

            if user.is_active:
                return redirect('login')

            user.is_active=True
            user.save()

            messages.success(request, 'Account activated successfully')
            return redirect('login')

        except Exception as e:
            pass

        return redirect('login')

class loginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = auth.authenticate(username=username, password=password)
            print(user)
            if user:
                print('true')
                if user.is_active:
                    print('is active')
                    auth.login(request, user)
                    messages.success(request, 'Logged in')
                    return redirect('/')
            print('error')
            messages.error(request, 'Invalid credentials')
            return redirect('login')
        messages.error(request, 'Please fill all fields')
        return redirect('login')

class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        messages.success(request, 'You have been logged out')
        return redirect('login')