from django.db import models
from .user import User                                                                                                                                                  

class Materia(models.Model):
    nome = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='materias')
    
    def __str__(self):
        return self.nome