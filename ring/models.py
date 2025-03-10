from django.db import models

class Anel(models.Model):
    NOME_MAX_LENGTH = 100
    PODER_MAX_LENGTH = 255
    PORTADOR_MAX_LENGTH = 100
    FORJADO_POR_MAX_LENGTH = 100
    IMAGEM_MAX_LENGTH = 255

    nome = models.CharField(max_length=NOME_MAX_LENGTH)
    poder = models.CharField(max_length=PODER_MAX_LENGTH)
    portador = models.CharField(max_length=PORTADOR_MAX_LENGTH)
    forjadoPor = models.CharField(max_length=FORJADO_POR_MAX_LENGTH)
    imagem = models.URLField(max_length=IMAGEM_MAX_LENGTH)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Anel"
        verbose_name_plural = "Anéis"