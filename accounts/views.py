from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, \
                    UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from orders.models import Order, Delivery, SupportTicket
from django.contrib.auth import get_user_model


User = get_user_model()

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
        else:
            form = LoginForm()
        return render(request, 'account/login.html', {'form': form})
    

@login_required
def dashboard(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    # Retrieve counts
    new_orders_count = Order.objects.filter(user=request.user, status=Order.Status.PENDING).count()
    delivered_orders_count = Order.objects.filter(user=request.user, status=Order.Status.DELIVERED).count()
    support_tickets_count = SupportTicket.objects.filter(user=request.user).count()

    return render(request, 'account/dashboard.html', {
        'section': 'dashboard',
        'user_form': user_form,
        'profile_form': profile_form,
        'new_orders_count': new_orders_count,
        'delivered_orders_count': delivered_orders_count,
        'support_tickets_count': support_tickets_count,
    })

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Создать новый объект пользователя,
            # но пока не сохранять его
            new_user = user_form.save(commit=False)
            # Установить выбранный пароль
            new_user.set_password(
            user_form.cleaned_data['password'])
            # Сохранить объект User
            new_user.save()
            # Создать профиль пользователя
            Profile.objects.create(user=new_user)
        return render(request, 'registration/register_done.html',{'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
        return render(request, 'registration/register.html', {'user_form': user_form})  