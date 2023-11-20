from django.shortcuts import render

# Create your views here.

desarrollado = 'Estudiantes Ingenieria de Software - Universidad Cooperativa de Colombia'
def index(request):
    return render(request, 'public/home.html', {
        'desarrollado': desarrollado
    })