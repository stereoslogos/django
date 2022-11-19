from django.shortcuts import render
from web.formularios.formularioPlatos import FormularioRegistroPlatos
from web.formularios.formularioEmpleados import FormularioRegistroEmpleados
from web.models import Idplatos
from web.models import Empleados

# Create your views here.
# Each view is a py function
def Home(request):
    return render(request, 'index.html')

def PlatosVista(request):
    # Load and render formularioPlatos
    formulario=FormularioRegistroPlatos()

    # Create a Dictionary to send data to the template
    diccionarioEnvioDatos = {
        'formulario':formulario
    }

    # Receive data from form REQ TYPE POST
    if request.method == 'POST':
        datosFormulario=FormularioRegistroPlatos(request.POST)
        if datosFormulario.is_valid():
            datosLimpios=datosFormulario.cleaned_data
            # Sending data to database
            platoNuevo=Idplatos(
                nombre=datosLimpios["nombrePlato"],
                descripcion=datosLimpios["descripcionPlato"],
                imagen=datosLimpios["fotoPlato"],
                precio=datosLimpios["precioPlato"],
                tipo=datosLimpios["tipoPlato"]
            )
            platoNuevo.save()

    return render(request, 'platos.html', diccionarioEnvioDatos)

def EmpleadosVista(request):
    formEmpl=FormularioRegistroEmpleados()
    dictEmpleados = {
        'form':formEmpl
    }
    if request.method == 'POST':
        dataEmpl=FormularioRegistroEmpleados(request.POST)
        if dataEmpl.is_valid():
            dataClean=dataEmpl.cleaned_data
            empleadoNuevo=Empleados(
                nameemployee = dataClean["nameEmployee"],
                lastemployee = dataClean["lastEmployee"],
                stateemployee = dataClean["stateEmployee"]

            )
            empleadoNuevo.save()
    
    return render(request, 'empleados.html', dictEmpleados)