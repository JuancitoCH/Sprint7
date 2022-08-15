from django.shortcuts import render,HttpResponse

from Login.models import client_auth_relation
from .models import Cliente
from django.contrib.auth.models import User
# Create your views here.
def createAllUsersTest(req):
    clientes = Cliente.objects.all()
    for cliente in clientes:
        print({
            'dni':cliente.customer_dni,
            'name':cliente.customer_name
        })
        user = User.objects.create_user(f'{cliente.customer_name}_{cliente.customer_dni}', f'{cliente.customer_dni}@hotmail.com', cliente.customer_dni)
        user.save()
        relation = client_auth_relation(client=cliente,auth=user)
        relation.save()
        
    # json.dumps({
    #     'hola':123
    # })
    return HttpResponse('Halo')