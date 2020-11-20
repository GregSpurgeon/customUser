from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login, logout
from myuser.models import MyUser
from myuser.forms import SignUpForm, LoginForm
# Create your views here.


def index_view(request):
    home = 'index.html'
    myuser = MyUser.objects.filter(id=request.user.id).first()
    return render(request, home, {"myusers": myuser})


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            MyUser.objects.create_user(
                username=data['username'],
                password=data['password'],
                display_name=data['display_name'],
                age=data['age'],
                homepage=data['homepage']
            )
            return redirect("/")
    form = SignUpForm()
    return render(request, "sign_up_form.html", {'form': form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,
                                username=data['username'],
                                password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next',
                                    reverse('home')))
    form = LoginForm()
    return render(request, 'sign_up_form.html', {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
