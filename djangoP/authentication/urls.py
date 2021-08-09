from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
from .views import RegistrationView, UsernameAuthentication, EmailAuthentication, verification, loginView

urlpatterns = [
    path('register', RegistrationView.as_view(), name='register'),
    path('login', loginView.as_view(), name='login'),
    path('validate-username', csrf_exempt(UsernameAuthentication.as_view()), name='validate-username'),
    path('validate-email', csrf_exempt(EmailAuthentication.as_view()), name='validate-email'),
    path('activate/<uidb64>/<token>', csrf_exempt(verification.as_view()), name='activate'),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)