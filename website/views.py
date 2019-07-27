from django.shortcuts import render
from website.models import Pessoa

# Create your views here.
def index(request):
    if request.method == 'POST':
        pessoa = Pessoa()
        pessoa.nome = request.POST.get('nome')
        pessoa.sobrenome = request.POST.get('sobrenome')
        pessoa.email = request.POST.get('email')
        pessoa.genero = request.POST.get('genero')
        pessoa.biografia = request.POST.get('biografia')
        pessoa.save()
        return render(request, 'login.html')

    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')