from django import forms
from usuarios.models import Usuario
from .models import Aluno

class UsuarioAlunoForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        label='Palavra-passe'
    )
    confirmar_password = forms.CharField(
        widget=forms.PasswordInput,
        label='Confirmar Palavra-passe'
    )

    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'username', 'email', 'telefone', 'foto']
        labels = {
            'first_name': 'Primeiro Nome',
            'last_name': 'Último Nome',
            'username': 'Nome de Utilizador',
            'email': 'Email',
            'telefone': 'Telefone',
            'foto': 'Foto',
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirmar = cleaned_data.get('confirmar_password')
        if password and confirmar and password != confirmar:
            raise forms.ValidationError('As palavras-passe não coincidem!')
        return cleaned_data


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['numero_matricula', 'categoria', 'instrutor', 'observacoes']
        labels = {
            'numero_matricula': 'Número de Matrícula',
            'categoria': 'Categoria',
            'instrutor': 'Instrutor',
            'observacoes': 'Observações',
        }