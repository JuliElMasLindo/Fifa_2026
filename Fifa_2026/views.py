from django.shortcuts import render
from django.shortcuts import redirect


from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate



from django.views import View

from .forms import RegisterForm

from equipo.models import Equipo

from tecnicos.models import Tecnico

from jugadores.models import Jugador

from django.shortcuts import get_object_or_404






def index(request):
    return render( request,'index.html', {
    } )
    
def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user: 
            login(request, user)
            messages.success(request, 'Bienvenido al Mundial')
            return redirect('index')
        else:
            messages.error(request, 'Usuario o Contraseña inválidos')
        
        
    return render(request, 'users/login.html', {'messages': messages.get_messages(request)
                                                
        
    })
    
def logout_view(request):
    logout(request)
    messages.success(request, 'Sessión cerrada exitosamente')
    return redirect('login')


def register(request):
    if request.user.is_authenticated:
        return redirect('index')
        
    form = RegisterForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        
        
        user = form.save()
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado Exitosamente')
            return redirect('index')
        

        
    return render(request, 'users/registro.html', {
        'form': form
    })
    
def equipo(request):
    
    equipos = Equipo.objects.all()
    
    return render( request,'equipo.html', {
        'equipos': equipos
    } )
    

def detalle_equipo(request, equipo_id):
    equipo = get_object_or_404(Equipo, pk=equipo_id)

    return render(request, 'users/detalle_equipo.html', {'equipo': equipo})


def jugador(request):
    
    jugadores = Jugador.objects.all()
    
    return render(request, 'jugadores.html',{
    }
    )
    
def contacto(request):
    return render( request,'contacto.html', {
    } )


def tecnico(request):
    
    tecnicos = Tecnico.objects.all()
    
    return render( request,'tecnicos.html', {
        'tecnicos': tecnicos
    } )
    