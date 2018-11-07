from django import forms
from apps.articles.models import Adoptante

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
