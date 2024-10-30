# views.py

from django.shortcuts import redirect, render
from django.contrib.auth import logout

def custom_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')  # Redireciona para a página de login após o logout
    return render(request, 'logout.html')  # Renderiza a página de logout para métodos GET