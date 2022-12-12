from django.db import models
import uuid


class Teams(models.Model):
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'
    F = 'F'
    G = 'G'
    H = 'H'
    Groups = [
            (A, 'Groupe A'),
            (B, 'Groupe B'),
            (C, 'Groupe C'),
            (D, 'Groupe D'),
            (E, 'Groupe F'),
            (F, 'Groupe F'),
            (G, 'Groupe G'),
            (H, 'Groupe EH')
            ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50,unique=True,null=False,blank=False)
    group = models.CharField(max_length=1,choices=Groups,null=False,blank=False)
    is_eliminated = models.BooleanField(default=True,null=False,blank=False)