from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
import json

# Create your views here.
class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')

class UsernameAuthentication(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error' : 'username should only contain alnumeric characters'})
        if User.objects.filter(username=username).exists():
            return JsonResponse({'usernamr_error' : 'username is not available'})
        return JsonResponse({'username_valid' : True})

