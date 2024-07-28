from django.db import models

# Create your models here.
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_positive(value):
    if value <= 0:
        raise ValidationError(
            _('%(value)s no es un número positivo'),
            params={'value': value},
        )

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_positive])
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def clean(self):
        if "@" not in self.email:
            raise ValidationError(_('El email debe contener @'))

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    productos = models.ManyToManyField(Producto)