from django.db import models


def content_file_name(instance, filename):
    print "INSTANCE(%s)" % instance._state.db
    return "/".join(instance._state.db, filename)


class Cliente(models.Model):

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    Nombre = models.CharField("Nombre", max_length=50)
    Foto = models.ImageField(upload_to=content_file_name)

    def __unicode__(self):
        return "Hello World"

    MY_FIELDS = ["Nombre", "Foto"]
