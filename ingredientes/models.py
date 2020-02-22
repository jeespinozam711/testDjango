# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

class Articulo(models.Model):
    Articulo = models.CharField( max_length=50,primary_key=True)
    Descripcion = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = '[fnica].[ARTICULO]'
    def __str__(self):
      return self.Descripcion

class Usuario(models.Model):
  Usuario= models.CharField(max_length=50, primary_key=True)
  Password =models.CharField(max_length=50)
  USERNAME_FIELD = "Usuario"
  class Meta:
    managed = False
    db_table='[fnica].[globalUsuario]'
  
  def get_username(self):
    return self.Usuario