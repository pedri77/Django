from django.contrib import messages
from django.contrib.auth import authenticate, login as login_user_in_django
from django.shortcuts import render, redirect


def login(request):

    if request.method == 'POST':
        username = request.POST.get('form_username')
        password = request.POST.get('form_password')
        user = authenticate(request, username=username, password=password)
        if user is None:  # si no existe el usuario con ese username/password
            messages.error(request, 'Wrong username or password')
        else:
            # si el usuario existe, tenemos que hacer login del usuario en la sesión
            login_user_in_django(request, user)
            return redirect('home')

    return render(request, 'users/login.html')
