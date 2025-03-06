from django.core.paginator import Paginator
from django.shortcuts import render, redirect


import empresa
from .forms import EmpleadoFormulario
from .models import Empleado, Departamento, Habilidad
#def crear_empleado(request):
#    if request.method == 'POST' and request.FILES:
#        nombre = request.POST['nombre']
#        fecha_nacimiento = request.POST['fecha_nacimiento']
#        antiguedad = request.POST['antiguedad']
#        departamento_id = request.POST['departamento']
#        habilidades_id = request.POST.getlist('habilidades')

#        departamento = Departamento.objects.get(id=departamento_id)
#        empleado = Empleado.objects.create(nombre=nombre,
#fecha_nacimiento=fecha_nacimiento, antiguedad=antiguedad,
#departamento=departamento)
#        empleado.habilidades.set(habilidades_id)
#        return redirect('listar_empleados')
#    departamentos = Departamento.objects.all()
#    habilidades = Habilidad.objects.all()
#    return render(request, 'empresa/crear_empleado.html' , {'departamentos': departamentos, 'habilidades': habilidades})

def crear_empleado(request, empleado=None):
    if request.method == 'POST' and request.FILES:
        form = EmpleadoFormulario(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Guarda el nuevo empleado con la imagen
            return redirect('listar_empleados')  # Redirige al listado en caso de
    else:
            form = EmpleadoFormulario()  # Si no es un POST, muestra el formulario vacío
    departamentos = Departamento.objects.all()
    habilidades = Habilidad.objects.all()
    return render(request, 'empresa/crear_empleado.html', {
        'form': form,
        'departamentos': departamentos,
        'habilidades': habilidades,
    })
def listar_empleados(request):
    empleados = Empleado.objects.all()
    paginator = Paginator(empleados, 5)
    page = request.GET.get('page')
    empleados_paginados = paginator.get_page(page)
    return render (request, 'empresa/listar_empleados.html' , {'empleados': empleados_paginados })


def ver_empleado(request, empleado_id):
    empleado = Empleado.objects.get(id=empleado_id)
    return render(request, 'empresa/ver_empleado.thml' , {'empleado': empleado})

def editar_empleado(request, empleado_id):
    empleado = Empleado.objects.get(id=empleado_id)
    if request.method == 'POST':
        empleado.nombre = request.POST['nombre']
        empleado.antiguedad = request.POST['antiguedad']
        departamento_id = request.POST['departamento']
        habilidades_ids = request.POST.getlist('habilidades')

        empleado.departamento = Departamento.objects.get(id=departamento_id)
        empleado.habilidades.set(habilidades_ids)
        empleado.save()
        return redirect('listar_empleados')

    departamentos = Departamento.objects.all()
    habilidades = Habilidad.objects.all()
    return render (request, 'empresa/editar_empleado.html', {
        'empleado': empleado,
        'departamentos': departamentos,
        'habilidades': habilidades,
    })

def eliminar_empleado(request, empleado_id):
    empleado = Empleado.objects.get(id=empleado_id)
    empleado.delete()
    return redirect('listar_empleados')