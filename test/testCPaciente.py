#import pytest

from src.cPaciente import *

def test_chequearEdad():
    aux_p = Paciente(4444444,"Lucia","Molina",21.9,"F",True,True,True,True)
    assert aux_p.verificar_edad(aux_p.edad) == "La edad no es un numero entero "
    aux_p1 = Paciente(4444444,"Lucia","Molina",-40,"F",True,True,True,True)
    assert aux_p1.verificar_edad(aux_p1.edad) == "La edad esta fuera de rango"
    aux_p2 = Paciente(4444444,"Lucia","Molina",200,"F",True,True,True,True)
    assert aux_p2.verificar_edad(aux_p2.edad) == "La edad esta fuera de rango"

def test_chequearNombreApellido():
    aux_p = Paciente(4444444,"!!","Molina",21,"F",True,True,True,True)
    assert aux_p.verifico_palabra(aux_p.nombre,aux_p.apellido) == "EL Nombre y/o Apellido es invalido"

def test_chequearGenero():
    aux_p = Paciente(4444444, "Lucia", "Molina", 21, "R", True, True, True, True)
    assert aux_p.verifico_genero(aux_p.genero) == "El genero es ivalido"

def test_chequearDNI():
    aux_p = Paciente(-4444444, "Lucia", "Molina", 21, "F", True, True, True, True)
    assert aux_p.verifico_dni(aux_p.dni) == "El DNI es menor a 0"

def test_chequearColorROJO():
    aux_p = Paciente(4444444, "Lucia", "Molina", 21, "F", True, False, True, True)
    aux_p.asignar_color()
    assert aux_p.Triage == Color.Rojo

def test_chequearColorNARANJA():
    aux_p = Paciente(4444444, "Lucia", "Molina", 21, "F", False, True, False, True)
    aux_p.asignar_color()
    assert aux_p.Triage == Color.Naranja

def test_chequearColorNARANJA2():
    aux_p = Paciente(4444444, "Lucia", "Molina", 21, "F", True, True, False, True)
    aux_p.asignar_color()
    assert aux_p.Triage == Color.Naranja

def test_chequearColorAMARILLO():
    aux_p = Paciente(4444444, "Lucia", "Molina", 21, "F", False, True, False, False)
    aux_p.asignar_color()
    assert aux_p.Triage == Color.Amarillo

def test_chequearColorAMARILLO2():
    aux_p = Paciente(4444444, "Lucia", "Molina", 21, "F", True, True, True, True)
    aux_p.asignar_color()
    assert aux_p.Triage == Color.Amarillo

def test_chequearColorVERDE():
    aux_p = Paciente(4444444, "Lucia", "Molina", 21, "F", False, True, True, True)
    aux_p.asignar_color()
    assert aux_p.Triage == Color.Verde

def test_chequearColorVERDE2():
    aux_p = Paciente(4444444, "Lucia", "Molina", 21, "F", True, True, True, False)
    aux_p.asignar_color()
    assert aux_p.Triage == Color.Verde

def test_chequearColorAZUL():
    aux_p = Paciente(4444444, "Lucia", "Molina", 21, "F", False, True, True, False)
    aux_p.asignar_color()
    assert aux_p.Triage == Color.Azul