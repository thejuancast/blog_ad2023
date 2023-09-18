from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Publicacion
from django.urls import reverse

# Create your tests here.
class PruebasBlog(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='usuarioPrueba',
            email='prueba@email.com',
            password='secreto'
        )

        cls.pub = Publicacion.objects.create(
            titulo='Un buen título',
            cuerpo='Un bonito contenido',
            autor=cls.user,
        )

    def test_modelo_publicacion(self):
        self.assertEqual(self.pub.titulo, 'Un buen título')
        self.assertEqual(self.pub.cuerpo, 'Un bonito contenido')
        self.assertEqual(self.pub.autor.username, 'usuarioPrueba')
        self.assertEqual(str(self.pub), 'Un buen título')
        self.assertEqual(self.pub.get_absolute_url(), '/pub/1/')

    def test_url_existe_ubicacion_correcta_listview(self):
        respuesta = self.client.get('/')
        self.assertEqual(respuesta.status_code, 200)

    def test_listview_publicacion(self):
        respuesta = self.client.get(reverse('inicio'))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, 'Un bonito contenido')
        self.assertTemplateUsed(respuesta, 'inicio.html')

    def test_detailview_publicacion(self):
        respuesta = self.client.get(reverse('detalle_publicacion', kwargs={'pk' : self.pub.pk}))
        sin_respuesta = self.client.get(reverse('detalle_publicacion', kwargs={'pk' : 100000}))
        sin_respuesta = self.client.get('/pub/100000/')
        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(sin_respuesta.status_code, 404)
        self.assertContains(respuesta, 'Un buen título')
        self.assertTemplateUsed(respuesta, 'detalle_publicacion.html')