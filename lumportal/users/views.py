from django.shortcuts import render,redirect
from .models import Oompa
# Create your views here.
def login(request):
    if request.method == "POST":
        name = request.POST.get('name')
        passw = request.POST.get('password')
        if name == "pushpagg" and passw == "pushpagg123":
            request.session["user"] = "pushpagg"
            return redirect("dashboard:dashboard")
        else:
            return render(request, "login.html", {"error": "Incorrect Credentials"})
    return render(request, "login.html")

def logout(request):
    request.session.flush()
    return redirect('users:login')


def oomplogin(request):
    if request.method == "POST":

        name = request.POST.get('name')
        passw = request.POST.get('password')
        if Oompa.objects.filter(name=name, passw=passw):
            request.session["user"] = name
            return redirect("dashboard:oompadashboard")
        else:
            return render(request, "oompalogin.html", {"error": "Incorrect Credentials"})
    return render(request, "oompalogin.html")
