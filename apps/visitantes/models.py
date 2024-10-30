from django.db import models


class Visitante(models.Model):

    STATUS_VISITANTE = (
        ("AGUARDANDO", "Aguardando autorização"),
        ("EM_VISITA", "Em visita"),
        ("FINALIZADO", "Visita finalizada")
    )

    status = models.CharField(
        verbose_name="Status do Visitante",
        max_length=10,
        choices=STATUS_VISITANTE,
        default="AGUARDANDO"
    )

    nome_completo = models.CharField(
        verbose_name="Nome Completo",
        max_length=255
    )

    cpf = models.CharField(
        verbose_name="CPF",
        max_length=11
    )

    data_nascimento = models.DateField(
        verbose_name="Data de Nascimento",
        auto_now=False,
        auto_now_add=False
    )

    numero_casa = models.PositiveSmallIntegerField(
        verbose_name="Número da Casa a ser visitada"
    )

    placa_veiculo = models.CharField(
        verbose_name="Placa do Veículo",
        max_length=7,
        blank=True,
        null=True
    )

    horario_chegada = models.DateTimeField(
        verbose_name="Horário de Chegada",
        auto_now=True,
    )

    horario_saida = models.DateTimeField(
        verbose_name="Horário de Saída",
        auto_now=False,
        blank=True,
        null=True
    )

    horario_autorizacao = models.DateTimeField(
        verbose_name="Horário de Autorização de entrada",
        auto_now=False,
        blank=True,
        null=True
    )

    morador_responsavel = models.CharField(
        verbose_name="Morador Responsável por Autorizar a Entrada do Visitante",
        max_length=255,
        blank=True
    )

    registrado_por = models.ForeignKey(
        "porteiros.Porteiros",
        verbose_name="Porteiro que registrou a entrada do visitante",
        on_delete=models.PROTECT
    )

    def get_horario_saida(self):
        if self.horario_saida:
            return self.horario_saida
        return "Horario de saida nao registrado"
    
    def get_horario_autorizacao(self):
        if self.horario_autorizacao:
            return self.horario_autorizacao
        return "Visitante aguardando autorizacao"
    
    def get_morador_responsavel(self):
        if self.morador_responsavel:
            return self.morador_responsavel
        return "Morador aguardando autorizacao"
    
    def get_placa_veiculo(self):
        if self.placa_veiculo:
            return self.placa_veiculo
        return "Veiculo nao registrado"
    
    def get_cpf(self):
        if self.cpf:
            cpf = str(self.cpf)

            return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

    class Meta:
        verbose_name = "Visitante"
        verbose_name_plural = "Visitantes"
        db_table = "visitantes"

    def __str__(self):
        return self.nome_completo