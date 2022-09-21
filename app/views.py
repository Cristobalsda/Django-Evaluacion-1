from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context

# Create your views here.

class Persona(object):
    def __init__(self, nombre, apellido, carrera, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.carrera = carrera
        self.edad = edad    

def index(request):
    return render(request,'web/index.html')

def usuarios(request):
    p1 = Persona('Cristobal', 'Pereira' , 'Ingenieria Informatica', '22')
    doc_externo = open('D:/programacion/programacion/Proyectos/back end/Django_Evaluacion_1/plantillas/web/usuario.html')
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    cont = Context({'nombre': p1.nombre, 'apellido': p1.apellido, 'carrera': p1.carrera, 'edad':p1.edad})
    docu = plantilla.render(cont)
    return HttpResponse(docu)
    
def juguetes(request):
    data = ({'titulo': 'jueguetes',
             'juguete1':'Muñeco Mario',
             'juguete2':'Juego de Herramientas',
             'juguete3':'Set de juguetes'})
    return (render(request, 'web/juguetes.html', data))

def ropa(request):
    data = ({'titulo': 'Ropa',
             'ropa1':'Chaqueta',
             'ropa2':'Pantalones',
             'ropa3':'Blusa'})
    return render(request, 'web/ropa.html', data)

def electronica(request):
    data = ({'titulo': 'ELECTRONICA',
             'ele1':'Televisor',
             'ele2':'Parlante',
             'ele3':'Proyector'})
    return render(request, 'web/electronica.html',data)

def categorias(request):
    return render(request, 'web/categorias.html')