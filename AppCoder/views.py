from xml.dom.minidom import Document
from django.shortcuts import render
from django.http import HttpResponse
from models import Curso


# Create your views here.
def curso(self):
    curso=curso(nombre="web", camada="1111")
    curso.save()
    documento= f"El curso es: {curso.nombre}, la camada:{curso.camada}"
    return HttpResponse(documento)
