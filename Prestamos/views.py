from pprint import pprint
from django.shortcuts import render,redirect
from Clientes.models import RelationClienteTipo
from django.contrib.auth.decorators import login_required
from Login.models import client_auth_relation

@login_required
def render_prestamos(req):
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
        if tipoCliente=='BLACK':
            if float(data['cantidad']) > 500000:
                return render(
            req,
            'prestamos/pre_aprobado_form.html',
            context={
            'render_message':True,
            'message':"Solicitud Rechazada Black",
            'cliente':tipoCliente
            }
        )
        if tipoCliente=='GOLD':
            if float(data['cantidad']) > 300000:
                return render(
                req,
                'prestamos/pre_aprobado_form.html',
                context={
                'render_message':True,
                'message':"Solicitud Rechazada Gold",
                'cliente':tipoCliente
                }
            )
        if tipoCliente=='CLASSIC':
            if float(data['cantidad']) > 100000:
                return render(
                req,
                'prestamos/pre_aprobado_form.html',
                context={
                'render_message':True,
                'message':"Solicitud Rechazada Classic",
                'cliente':tipoCliente
                }
            )
        # pprint(dir(tipoCliente))
        return render(
            req,
            'prestamos/pre_aprobado_form.html',
            context={
            'render_message':True,
            'message':"Solicitud",
            'cliente':tipoCliente
            }
        )
    else:
        return redirect('form_preap_prestamos')