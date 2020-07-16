from django.contrib import admin
from django.urls import path, include
from core.forms import CustomUserForm
from django_registration.backends.one_step.views import RegistrationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register', RegistrationView.as_view(
        form_class=CustomUserForm,
        success_url='/'
    ), name='register'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/auth/', include('rest_auth.urls')),
    path('api/auth/registration/', include('rest_auth.registration.urls')),
]
