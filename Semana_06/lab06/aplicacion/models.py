from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre= models.CharField(max_length=100)
    pub_date= models.DateTimeField("Fecha de registro",auto_now_add=True)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    categoria= models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre= models.CharField(max_length=200)
    precio=models.DecimalField(max_digits=6,decimal_places=2) 
    stock=models.IntegerField(default=0)
    pub_date= models.DateTimeField("date published")
    imagen = models.ImageField(upload_to="productos", null=True)
    descripcion = models.TextField(null=True)
    def __str__(self):
        return self.nombre
    