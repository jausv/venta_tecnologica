from django.contrib import admin

# Register your models here.
from .models import Producto, Cliente, Venta

admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Venta)

