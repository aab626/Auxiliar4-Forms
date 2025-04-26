from django import forms
from .models import Categoria, Tarea

class NuevaTareaForm(forms.Form):
    titulo = forms.CharField(label='Título de la tarea')
    contenido = forms.CharField(widget=forms.Textarea())
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all())

class NuevaTareaModelForm(forms.ModelForm):
    titulo = forms.CharField(label='Override de label titulo')
    
    class Meta:
        model = Tarea
        fields = ['titulo', 'contenido', 'categoria']

    def clean_titulo(self):
        field = self.cleaned_data.get('titulo')
        if not "Tarea" in field:
            raise forms.ValidationError('Debe incluir el texto \'Tarea\'')
        
        return field