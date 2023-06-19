from django.contrib import admin
from .models import Leitor, Livro, Emprestimo

# Register your models here.

admin.site.register(Leitor)
admin.site.register(Livro)
admin.site.register(Emprestimo)