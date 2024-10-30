from django.db import models

class Porteiros(models.Model):

    usuario = models.OneToOneField(
        "usuarios.Usuario",
        on_delete=models.PROTECT,
        verbose_name="Usuário",
    )

    nome_completo = models.CharField(
        verbose_name="Nome Completo",
        max_length=200,
    )

    cpf = models.CharField(
        verbose_name="CPF",
        max_length=11,
    )

    telefone = models.CharField(
        verbose_name="Telefone de contato",
        max_length=11,
    )

    data_nascimento = models.DateField(
        verbose_name="Data de Nascimento",
        auto_now=False,
        auto_now_add=False,
    )

    class Meta:
        verbose_name = "Porteiro"
        verbose_name_plural = "Porteiros"
        db_table = "porteiro"

    def __str__(self):
        return self.nome_completo
