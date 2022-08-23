from pprint import pprint
from django.shortcuts import render
from Cuentas.models import Cuenta
from Login.models import client_auth_relation
# Create your views here.
def home(req):
    # pprint(dir(req.user))
    context={}
    if req.user.is_authenticated:
        clientid = client_auth_relation.objects.get(auth_id=req.user.pk).client_id
        # tipo uno cuenta en pesos
        cuentas_cliente = Cuenta.objects.all().filter(customer_id=clientid,tipo=1)
        print(cuentas_cliente[0])
        if not cuentas_cliente[0]:
            context={'balance':'X'}
        else: 
            context={ 'balance':float(cuentas_cliente[0].balance) /100}

    # if :
    return render(req,'home/home.html',context=context)

def dolar(req):
    return render(req,'home/dolar.html')