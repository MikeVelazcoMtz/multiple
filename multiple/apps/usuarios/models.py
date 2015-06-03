from django.db import models, router
from multiple.utils import content_file_name


class Cliente(models.Model):

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    Nombre = models.CharField("Nombre", max_length=50)
    Foto = models.ImageField(upload_to=content_file_name)

    def __unicode__(self):
        return "%s" % (self.Nombre)

    MY_FIELDS = ["Nombre", "Foto"]
