from django.test import TestCase
from .models import Anel

class AnelModelTest(TestCase):

    def setUp(self):
        Anel.objects.create(
            nome="Narya, o anel do fogo",
            poder="Seu portador ganha resistência ao fogo",
            portador="Gandalf",
            forjadoPor="Elfos",
            imagem="http://example.com/narya.jpg"
        )

    def test_anel_creation(self):
        anel = Anel.objects.get(nome="Narya, o anel do fogo")
        self.assertEqual(anel.poder, "Seu portador ganha resistência ao fogo")
        self.assertEqual(anel.portador, "Gandalf")
        self.assertEqual(anel.forjadoPor, "Elfos")
        self.assertEqual(anel.imagem, "http://example.com/narya.jpg")

    def test_anel_update(self):
        anel = Anel.objects.get(nome="Narya, o anel do fogo")
        anel.portador = "Frodo"
        anel.save()
        updated_anel = Anel.objects.get(nome="Narya, o anel do fogo")
        self.assertEqual(updated_anel.portador, "Frodo")

    def test_anel_deletion(self):
        anel = Anel.objects.get(nome="Narya, o anel do fogo")
        anel.delete()
        with self.assertRaises(Anel.DoesNotExist):
            Anel.objects.get(nome="Narya, o anel do fogo")