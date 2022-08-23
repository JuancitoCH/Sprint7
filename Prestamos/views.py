from pprint import pprint
from django.shortcuts import render,redirect
from Clientes.models import RelationClienteTipo
from django.contrib.auth.decorators import login_required
from Login.models import client_auth_relation
from Cuentas.models import Cuenta,TiposCuenta
from .models import Prestamo
from django.db.models import F

@login_required
def render_prestamos(req):
    try:
        client = client_auth_relation.objects.get(auth_id=req.user.pk).client_id
        prestamos = Prestamo.objects.all().filter(customer_id=client)
        # print(prestamos)
        # pprint(dir(prestamos))
        return render(req,'prestamos/prestamos_page.html',context={
            "prestamos":prestamos
        })
    except:
        return render(req,'prestamos/prestamos_page.html')

@login_required
def formulario_prestamos_preaprobados(req):
    client = client_auth_relation.objects.get(auth_id=req.user.pk).client_id
    tipoCliente = RelationClienteTipo.objects.get(fk_cliente=client).fk_tipos_cliente.tcli_tipo
    print(tipoCliente)

    return render(
    req,
    'prestamos/pre_aprobado_form.html',
    context={
        'render_message':False,
        'cliente':tipoCliente
    }
)


@login_required
def formulario_prestamos_preaprobados_POST(req):
    # pprint(dir(req.body))
    data = req.POST
    if req.POST:
        client = client_auth_relation.objects.get(auth_id=req.user.pk).client_id
        tipoCliente = RelationClienteTipo.objects.get(fk_cliente=client).fk_tipos_cliente.tcli_tipo
        print(tipoCliente)
        # pprint(dir(tipoCliente))
        response = tipoDeClienteRestricciones(data=data,tipoCliente=tipoCliente,clientid=client)
        if response.get('redirect') :
            return redirect('prestamos_page')
        return render(
        req,
        'prestamos/pre_aprobado_form.html',
        context=response
    )
        
    else:
        return redirect('form_preap_prestamos')

def tipoDeClienteRestricciones(tipoCliente,data,clientid):
    tipos = {
        "CLASSIC":100000,
        "GOLD":300000,
        "BLACK":500000,
    }
    cantidad = float(data['cantidad']) if data['cantidad'] else 0
    if cantidad <= tipos.get(tipoCliente,0) and cantidad!=0:
        Prestamo.objects.create(
            loan_date=data['fecha'],
            loan_type=data['tipo_prestamo'],
            loan_total=cantidad*100,
            customer_id=clientid
        ).save()
        # caja de ahorro en pesos 1
        cuentas = Cuenta.objects.all().filter(customer_id=clientid,tipo=1)
        print(cuentas)
        # si la cuenta de pesos no existe la creamos
        if not cuentas :
            Cuenta.objects.create(
                customer_id=clientid,
                balance=cantidad*100,
                iban='null',
                tipo=TiposCuenta.objects.get(tcu_id=1)
                ).save()
        else:
            # contrario sumamos la cantidad al balance de la cuenta en pesos
            cuentas = Cuenta.objects.filter(customer_id=clientid,tipo=1).update(balance=F('balance')+cantidad)
            
        return {
        'redirect':True,
        'render_message':True,
        'aproved':True,
        'message':"Solicitud Aceptada",
        'cliente':tipoCliente
    }
    else:
        return {
        'render_message':True,
        'aproved':False,
        'message':"Solicitud Rechazada",
        'cliente':tipoCliente
    }