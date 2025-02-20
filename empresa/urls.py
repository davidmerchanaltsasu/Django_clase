from django.urls import path
from .views import listar_empleados, crear_empleado, editar_empleado, eliminar_empleado, ver_empleado

urlpatterns = [
    path('empleados/crear/', crear_empleado, name='crear_empleado'),
    path('empleados/', listar_empleados, name='listar_empleados'),

    path('empleados/<int:empleado_id>', ver_empleado, name='ver_empleado'),

    path('empleados/editar/<int:empleado_id>', editar_empleado, name='editar_empleado'),

    path('empleados/eliminar/<int:empleado_id>', eliminar_empleado, name='eliminar_empleado'),

]

