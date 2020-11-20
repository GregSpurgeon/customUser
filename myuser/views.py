from django.shortcuts import render
from myuser.models import MyUser
# Create your views here.


def index_view(request):
    home = 'index.html'
    myuser = MyUser.objects.first()
    return render(request, home, {"myusers": myuser})