from django.shortcuts import render
from web.formularios.formularioPlatos import FormularioRegistroPlatos
from web.formularios.formularioEmpleados import FormularioRegistroEmpleados

# Create your views here.
# Each view is a py function
def Home(request):
    return render(request, 'index.html')

def Platos(request):
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
            print(datosLimpios)

    return render(request, 'platos.html', diccionarioEnvioDatos)

def Empleados(request):
    formEmpl=FormularioRegistroEmpleados()
    dictEmpleados = {
        'form':formEmpl
    }
    if request.method == 'POST':
        dataEmpl=FormularioRegistroEmpleados(request.POST)
        if dataEmpl.is_valid():
            dataClean=dataEmpl.changed_data
            print(dataClean)
    
    return render(request, 'empleados.html', dictEmpleados)