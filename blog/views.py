from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy #
from .models import Publicacion

# Create your views here.
class VistaListaBlog(ListView):
    model = Publicacion
    template_name = 'inicio.html'

class VistaDetalleBlog(DetailView):
    model = Publicacion
    template_name = 'detalle_publicacion.html'
    context_object_name = 'publicacion'

class VistaCrearEntradaBlog(CreateView):
    model = Publicacion
    template_name = 'pub_nueva.html'
    fields = ['titulo', 'autor', 'cuerpo']

class VistaEditarEntradaBlog(UpdateView):
    model = Publicacion
    template_name = 'editar_pub.html'
    fields = ['titulo', 'cuerpo']

class VistaEliminarEntradaBlog(DeleteView):
    model = Publicacion
    template_name = 'eliminar_pub.html'
    success_url = reverse_lazy('inicio') # Se usa reverse lazy porque con reverse no se espera a que la base de datos responda y aún muestra la publicación que se elimino