from django.db import models
from uuid import uuid4

# Create your models here.


def upload_image_book(instance, filename):
    return f"{instance.id_book}-{filename}"

def __str__(self):
    return self.title



class Books(models.Model):
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(verbose_name="Título", max_length=255)
    author = models.CharField(verbose_name="Autor",max_length=255)
    release_year = models.IntegerField(verbose_name="Ano de lançamento",)
    state = models.CharField(verbose_name="Estado de conservação",max_length=50)
    pages = models.IntegerField(verbose_name="Nº de páginas",)
    publishing_company = models.CharField(verbose_name="Editora",max_length=255)
    create_at = models.DateField(verbose_name="Data de criação",auto_now_add=True)
    image = models.ImageField(verbose_name="Imagem", upload_to=upload_image_book, blank=True, null=True)