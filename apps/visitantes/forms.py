from django import forms
from visitantes.models import Visitante

class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = [
            "nome_completo",
            "cpf",
            "data_nascimento",
            "numero_casa",
            "placa_veiculo",
        ]
        error_messages = {
            "nome_completo": {
                "required": "O campo nome completo é obrigatório."
            },
            "cpf": {
                "required": "O campo CPF é obrigatório."
            },
            "data_nascimento": {
                "required": "O campo data de nascimento é obrigatório.",
                "invalid": "Data de nascimento inválida."
            },
            "numero_casa": {
                "required": "O campo número da casa é obrigatório."
            },
            "placa_veiculo": {
                "required": "O campo placa do veículo é obrigatório."
            }
        }

class AutorizaVisitanteForm(forms.ModelForm):
    morador_responsavel = forms.CharField(required=True)

    class Meta:
        model = Visitante
        fields = [
            "morador_responsavel",
        ]
        error_messages = {
            "morador_responsavel": {
                "required": "Por favor, informe o nome do morador responsável por autorizar o visitante."
            },
        }
