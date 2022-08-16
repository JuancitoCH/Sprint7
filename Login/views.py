from django.shortcuts import  render, redirect,HttpResponse

from .models import client_auth_relation
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registro exitoso." )
			return redirect("/")
		messages.error(request, "Registro fallido. Informacion invalida.")
	form = NewUserForm()
	return render (request = request, template_name = "registration/register.html", context = { "register_form": form })

def muestra(req):
	print(client_auth_relation.objects.all())
	return HttpResponse('a')