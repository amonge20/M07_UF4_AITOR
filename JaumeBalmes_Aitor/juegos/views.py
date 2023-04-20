from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import PersonForm
from django.shortcuts import render, redirect

def user_form(request):
    form = PersonForm()
    context = {'form':form}
    return render(request, "form.html", context)
def alumneForm(request):
    form = AlumneForm()
    form = AlumneForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('stdnts')

    context = {'form': form}
    return render(request, 'alumneForm.html', context)

def profeForm(request):
    form = ProfeForm()
    form = ProfeForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('tchrs')

    context = {'form': form}
    return render(request, 'profeForm.html', context)



def index(request):
   template = loader.get_template('index.html')
   return HttpResponse(template.render())

def teachers(request):
    context = {"prof": profList}
    return render(request, 'teachers.html', context)

def students(request):
    context = {"alumn": alumnList}
    return render(request, 'students.html', context)
def teacher(request, pk):
    teacher_Obj = None
    for t in profList:
        if t['id'] == int(pk):
            teacher_Obj = t
    return render(request, 'teacher.html', {'thcr':teacher_Obj})
def student(request, pk):
    student_Obj = None
    for s in alumnList:
        if s['id'] == int(pk):
            student_Obj = s
    return render(request, 'student.html', {'stdnt':student_Obj})
# Añadiremos un JSON para recopilar la lista de profes y alumnos
# Lista Profes
profList = [
    {
        "id": 1,
        "name":"Aitor",
        "surname":"Monge",
        "age": 21,
    },
    {
        "id": 2,
        "name": "Kevin",
        "surname": "Sabana",
        "age": 23,
    },
    {
        "id": 3,
        "name": "Joan",
        "surname": "Josep",
        "age": 25,
    }]
# Lista Alumnos
alumnList = [
    {
        "id": 1,
        "name": "Raul",
        "surname": "Vaquerufo",
        "age": 35,
    },
    {
        "id": 2,
        "name": "Paco",
        "surname": "Sanchez",
        "age": 45,
    },
    {
        "id": 3,
        "name": "Luis",
        "surname": "Manuel",
        "age": 26,
    },
    {
        "id": 4,
        "name": "Miguel",
        "surname": "Angel",
        "age": 30,
    },
    {
        "id": 5,
        "name": "Michael",
        "surname": "John",
        "age": 49,
    },
    {
        "id": 6,
        "name": "Yelly",
        "surname": "Bone",
        "age": 25,
    }]