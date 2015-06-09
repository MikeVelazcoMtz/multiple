from django.db import models
from multiple.utils import NMImageField


class Cliente(models.Model):

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    Nombre = models.CharField("Nombre", max_length=50)
    Foto = NMImageField()

    def __unicode__(self):
        return "%s" % (self.Nombre)

    MY_FIELDS = ["Nombre", "Foto"]
