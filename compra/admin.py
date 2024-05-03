from django.contrib import admin
from .models import Producto, Proveedor


# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'proveedor',]


class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido',]


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Proveedor, ProveedorAdmin)