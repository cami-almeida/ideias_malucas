from django.shortcuts import render, redirect
from website.models import Pessoa, Ideia

# Create your views here.
def index(request):
    if request.method == 'POST':
        pessoa = Pessoa()
        pessoa.nome = request.POST.get('nome')
        pessoa.sobrenome = request.POST.get('sobrenome')
        pessoa.email = request.POST.get('email')
        pessoa.genero = request.POST.get('genero')
        pessoa.biografia = request.POST.get('biografia')
        pessoa.senha = request.POST.get('senha')
        pessoa.save()
        return render(request, 'login.html')

    return render(request, 'index.html')

def __str__(self):
    return self.nome + ' ' + self.sobrenome

def login(request):
    if request.method == 'POST':
        email_form = request.POST.get('email')
        senha_form = request.POST.get('senha')
        pessoa = Pessoa.objects.filter(email=email_form, senha=senha_form).first()

        if pessoa is None:
            contexto = {'msg': 'Cadastre-se para criar uma ideia'}
            return render(request, 'index.html', contexto)
        else:
            contexto = {'pessoa': pessoa}
            return render(request, 'ideias.html', contexto)

    return render(request, 'login.html', {})

def ideias(request):
    if request.method == 'POST':
        email_pesssoa = request.POST.get('email')
        pessoa = Pessoa.objects.filter(email=email_pesssoa).first()
        if pessoa is not None:
            ideia = Ideia()
            ideia.pessoa = pessoa
            ideia.titulo = request.POST.get('titulo')
            ideia.descricao = request.POST.get('descricao')
            ideia.categoria = request.POST.get('categoria')
            ideia.categoria_outros = request.POST.get('categoria_outros')
            ideia.save()
            return redirect('/lista') 

    return(request,'ideias.html')

def lista(request):    
    ideias = Ideia.objects.all()
    contexto = {
        'ideias': ideias
    }
    return render(request, 'lista.html', contexto)
