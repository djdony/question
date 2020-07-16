from django_registration.forms import RegistrationForm
from core.models import User


class CustomUserForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = User
