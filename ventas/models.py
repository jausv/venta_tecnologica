from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre
    


# class Venta(models.Model):
#     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
#     producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
#     cantidad = models.IntegerField()
#     fecha = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'{self.cantidad} x {self.producto.nombre} para {self.cliente.nombre}'


class Venta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Relación con Cliente
    cantidad = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Antes de guardar, verificar si hay suficiente stock
        if self.producto.stock >= self.cantidad:
            self.producto.stock -= self.cantidad  # Reducir el stock del producto
            self.producto.save()  # Guardar los cambios en el stock del producto
            super().save(*args, **kwargs)  # Guardar la venta
        else:
            raise ValueError('Stock insuficiente para esta venta')

    def __str__(self):
        return f'Venta de {self.cantidad} {self.producto.nombre} a {self.cliente.nombre}'


