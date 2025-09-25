from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Usuario
from .forms import UsuarioForm

@login_required
def index(request):
    usuarios=Usuario.objects.all()
    return render(request,'usuarios/index.html',{'usuarios':usuarios})

@login_required
def create(request):
    if request.method=='POST':
        form=UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=UsuarioForm()
    return render(request,'usuarios/form.html',{'form':form,'titulo':'Nuevo Usuario'})

@login_required
def edit(request,id):
    usuario=get_object_or_404(Usuario,id=id)
    if request.method=='POST':
        form=UsuarioForm(request.POST,instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=UsuarioForm(instance=usuario)
    return render(request,'usuarios/form.html',{'form':form,'titulo':'Editar Usuario'})

@login_required
def delete(request,id):
    usuario=get_object_or_404(Usuario,id=id)
    usuario.delete()
    return redirect('index')
