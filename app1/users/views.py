from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from users.forms import UserLoginForm, UserRegisterForm, ProfileForm


def login(request) -> HttpResponse:
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, successfully logged in!")
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
    context: dict[str, str] = {
        'title': 'Home - Авторизация',
        'form': form
    }

    return render(request, 'users/login.html', context)


def registration(request) -> HttpResponse:
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f"{user.username}, successfully registrated in!")
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegisterForm()

    context: dict[str, str] = {
        'title': 'Home - Регистрация',
        'form': form,
    }

    return render(request, 'users/registration.html', context)


@login_required
def profile(request) -> HttpResponse:
    from orders.models import Order
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Профиль успешно обновлен")
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = ProfileForm(instance=request.user)
        
    orders = Order.objects.filter(user=request.user).prefetch_related('orderitem_set').order_by('-id')
    
    context = {
        'title': 'Home - Кабинет',
        'form': form,
        'orders': orders,
    }

    return render(request, 'users/profile.html', context)

@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, log out")
    auth.logout(request)
    return redirect(reverse('main:index'))
