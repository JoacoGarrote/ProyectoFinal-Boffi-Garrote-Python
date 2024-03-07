from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text="Ingrese un correo electronico válido.")
    first_name = forms.CharField(max_length=30, required=True, help_text="Campo obligatorio.")
    last_name = forms.CharField(max_length=30, required=True, help_text="Campo obligatorio.")
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'profile_picture']


class UserEditForm(UserChangeForm):
    email = forms.EmailField(max_length=254, required=True, help_text="Ingrese un correo electronico válido.")
    first_name = forms.CharField(max_length=30, required=True, help_text="Campo obligatorio.")
    last_name = forms.CharField(max_length=30, required=True, help_text="Campo obligatorio.")
    profile_picture = forms.ImageField(required=False)
    description = forms.CharField(required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'profile_picture', 'description']


class PasswordChangeForm(forms.Form):
    old_password = forms.CharField(label='Contraseña actual', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='Nueva contraseña', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Confirmar nueva contraseña', widget=forms.PasswordInput)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.user.check_password(old_password):
            raise forms.ValidationError('La contraseña actual es incorrecta.')
        return old_password

    def clean_new_password2(self):
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.cleaned_data.get('new_password2')
        if new_password1 != new_password2:
            raise forms.ValidationError('Las nuevas contraseñas no coinciden.')
        return new_password2