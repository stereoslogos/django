from django import forms

class FormularioRegistroEmpleados(forms.Form):
    STATE=(
        (1, 'Single'),
        (2, 'Married'),
        (3, 'Widow')
    )
    nameEmployee=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=25,
        required=True,
        label='Name'
    )
    lastEmployee=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=25,
        required=True,
        label='Last'
    )
    stateEmployee=forms.ChoiceField(
        widget=forms.Select(attrs={"class":"form-control mb-3"}),
        label='Marital status',
        choices=STATE
    )

