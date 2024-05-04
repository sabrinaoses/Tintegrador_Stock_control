from django import forms
from .models import Producto, Proveedor
from django.shortcuts import render, get_object_or_404, redirect, reverse

class ProductoForm(forms.ModelForm):

    producto = forms.ModelChoiceField(queryset=Producto.objects.all())

    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock_actual', 'proveedor']


class ProductoEditForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock_actual']


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        verbose_name_plural = "proveedores"
        fields = ['nombre', 'apellido', 'dni']


class ProveedorEditForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        verbose_name_plural = "proveedores"
        fields = ['nombre', 'apellido']