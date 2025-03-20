from autenticacion.views import registrar
from django.urls import path
urlpatterns = [
    path('registro/', registrar, name='registro'),
    path( 'logout/', logout, name='logout' ),
]