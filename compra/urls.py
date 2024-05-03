from django.urls import path
from .views import  agregar_proveedor, agregar_producto, listar_proveedor, listar_productos, actualizar_producto, \
    actualizar_proveedor

app_name = 'compra'

urlpatterns = [

    path('', listar_proveedor, name="listar_proveedor"),
    path('agregar_proveedor/', agregar_proveedor, name='agregar_proveedor'),
    path('agregar_producto /', agregar_producto, name='agregar_producto'),
    path('listar_proveedor/', listar_proveedor, name="listar_proveedor"),
    path('listar_productos/', listar_productos, name="listar_productos"),
    path('actualizar_producto/<int:pk>', actualizar_producto, name="actualizar_producto"),
    path('actualizar_proveedor/<int:pk>', actualizar_proveedor, name="actualizar_proveedor"),

]
