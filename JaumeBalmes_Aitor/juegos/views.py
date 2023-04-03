from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
   template = loader.get_template('index.html')
   return HttpResponse(template.render())

def teachers(request):
    context = {"prof": profList}
    return render(request, 'teachers.html', context)

def students(request):
    context = {"alumn": alumnList}
    return render(request, 'students.html', context)

# Añadiremos un JSON para recopilar la lista de profes y alumnos
# Lista Profes
profList = [
    {
        "name":"Aitor",
        "surname":"Monge",
        "age":"21",
    },
    {
        "name": "Kevin",
        "surname": "Sabana",
        "age":"23",
    },
    {
        "name": "Joan",
        "surname": "Josep",
        "age": "25",
    }]
# Lista Profes
alumnList = [
    {
        "name": "Raul",
        "surname": "Vaquerufo",
        "age": "35",
    },
    {
        "name": "Paco",
        "surname": "Sanchez",
        "age": "45",
    },
    {
        "name": "Luis",
        "surname": "Manuel",
        "age": "26",
    },
    {
        "name": "Miguel",
        "surname": "Angel",
        "age": "30",
    },
    {
        "name": "Michael",
        "surname": "John",
        "age": "49",
    },
    {
        "name": "Yelly",
        "surname": "Bone",
        "age": "25",
    }]