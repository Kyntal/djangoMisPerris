from django import forms
from articles.models import Adoptante
from django.contrib.auth.models import User

class AdoptanteForm(forms.ModelForm):
    class Meta:
        model = Adoptante

        fields = [
            'rut_adop',
            'nomb_adoptante',
            'apaterno_adoptante',
            'correo_adoptante',
            'edad_adoptante',
            'tel_adoptante',
        ]
        labels = {
            'rut_adop': 'Rut Adoptante',
            'nomb_adoptante': 'Nombre',
            'apaterno_adoptante': 'Apellido',
            'correo_adoptante': 'Correo',
            'edad_adoptante': 'Edad',
            'tel_adoptante': 'Teléfono',
        }
        widgets = {
            'rut_adop': forms.TextInput(attrs={'class':'form-control'}),
            'nomb_adoptante': forms.TextInput(attrs={'class':'form-control'}),
            'apaterno_adoptante': forms.TextInput(attrs={'class':'form-control'}),
            'correo_adoptante': forms.TextInput(attrs={'class':'form-control'}),
            'edad_adoptante': forms.TextInput(attrs={'class':'form-control'}),
            'tel_adoptante': forms.TextInput(attrs={'class':'form-control'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Contraseña',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repite Contraseña',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
