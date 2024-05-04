
from .models import Proveedor, Producto
from .forms import ProductoForm, ProveedorForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, reverse


def agregar_producto(request):
    nuevo_producto = None
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST)
        if producto_form.is_valid():
            # Se guardan los datos que provienen del formulario en la B.D.
            nuevo_producto = producto_form.save(commit=True)
            messages.success(request,
                             'Se ha agregado correctamente el producto{}'.format(nuevo_producto))
            return redirect(reverse('producto:agregar_producto', args={nuevo_producto.id}))
    else:
        producto_form = ProductoForm()

    return render(request, 'compra/agregar_producto.html',
                         {'form': agregar_producto})


def agregar_proveedor(request):
    nuevo_proveedor = None
    if request.method == 'POST':
        proveedor_form = ProductoForm(request.POST)
        if proveedor_form.is_valid():
            # Se guardan los datos que provienen del formulario en la B.D.
            nuevo_proveedor = proveedor_form.save(commit=True)
            messages.success(request,
                             'Se ha agregado correctamente el proveedor{}'.format(nuevo_proveedor))
            return  redirect(reverse('proveedor:agregar_proveedor', args={nuevo_proveedor.id}))
    else:
        proveedor_form = ProveedorForm()

    return render(request, 'compra/agregar_proveedor.html',
                         {'form': agregar_proveedor})


#Crear proveedor

#def agregar_proveedor(request):
 #   form = forms.ProveedorForm()
  #  if request.method == 'POST':
   #     form = forms.ProveedorForm(request.POST)
    #    if form.is_valid():
     #       form.save()
    #return django.shortcuts.render(request, 'compra/agregar_proveedor.html', {'form': form})



#Crear producto

#def agregar_producto(request):

 #   form = forms.ProductoForm(proveedor_choices=Proveedor.objects.all())
  #  if request.method == 'POST':
   #     form = forms.ProductoForm(request.POST, proveedor_choices=Proveedor.objects.all())
    #    if form.is_valid():
     #       form.save()
    #return django.shortcuts.render(request, 'compra/agregar_producto.html', {'form': form, 'proveedores': Proveedor.objects.all()})




#Listar todos los proveedores

def listar_proveedor(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'compra/listar_proveedor.html', {'proveedores': proveedores})


#Listar todos los productos

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'compra/listar_productos.html', {'productos': productos})


#Actualizar Productos

def actualizar_producto(request, pk):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')

        producto = Producto.objects.get(pk=pk)
        producto.nombre = nombre
        producto.precio = precio
        producto.stock = stock
        producto.save()

        productos = Producto.objects.all()
        return render(request, 'listar_productos.html', {'productos': productos})

    else:
        producto = Producto.objects.get(pk=pk)
        return render(request, 'listar_productos.html', {'producto': producto})

#Actualizar Proveedor


def actualizar_proveedor(request, pk):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        dni = request.POST.get('dni')

        proveedor = Proveedor.objects.get(pk=pk)
        proveedor.nombre = nombre
        proveedor.apellido = apellido
        proveedor.dni = dni
        proveedor.save()

        proveedores = Proveedor.objects.all()
        return render(request, 'listar_proveedor.html', {'proveedores': proveedores})

    else:
        proveedor = Proveedor.objects.get(pk=pk)
        return render(request, 'actualizar_proveedor.html', {'proveedor': proveedor})


#Borrar producto

def borrar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
    return redirect('listar_productos')


#Borrar proveedor

def borrar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
    return redirect('listar_proveedor')