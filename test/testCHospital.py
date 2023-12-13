from src.cHospital import *

def chequear_ingreso_pac():
    aux_h = Hospital()
    aux_p = Paciente(4444444, "Lucia", "Molina", 21, "F", False, True, True, False)
    aux_h.agregar_persona(aux_p)
    assert aux_h.cola_pac[0] is not None

def chequear_ingreso_pac2():
    aux_h = Hospital()
    aux_p = Paciente(4444444, "Lucia", "Molina", 21, "F", False, True, True, False)
    aux_h.agregar_persona(aux_p)
    aux_p1 = Paciente(4464444, "MAria", "Pereyra", 21, "F", False, True, True, False)
    aux_p2 = Paciente(22, "Pablo", "R", 21, "F", False, True, True, False)
    aux_p3 = Paciente(9987, "Martin", "P", 21, "F", False, True, True, False)
    aux_h.agregar_persona(aux_p1)
    aux_h.agregar_persona(aux_p2)
    aux_h.agregar_persona(aux_p3)
    assert aux_h.cola_pac[0] is not None
    assert aux_h.cola_pac[1] is not None
    assert aux_h.cola_pac[2] is not None
    assert aux_h.cola_pac[3] is not None

def chequear_ingreso_pacREPETIDOS():
    aux_h = Hospital()
    aux_p = Paciente(4444444, "Lucia", "Molina", 21, "F", False, True, True, False)
    aux_h.agregar_persona(aux_p)
    aux_p1 = Paciente(4464444, "MAria", "Pereyra", 21, "F", False, True, True, False)
    aux_p2 = Paciente(22, "Pablo", "R", 21, "F", False, True, True, False)
    aux_p3 = Paciente(9987, "Martin", "P", 21, "F", False, True, True, False)
    aux_h.agregar_persona(aux_p1)
    aux_h.agregar_persona(aux_p2)
    aux_h.agregar_persona(aux_p3)
    assert aux_h.cola_pac[0] is not aux_p3
    assert aux_h.cola_pac[1] is not aux_p
    assert aux_h.cola_pac[2] is not aux_p1
    assert aux_h.cola_pac[3] is not aux_p2

def chequear_ingreso_consultorio():
    aux_h = Hospital()
    aux_c = Consultorio(1)
    aux_h.agregar_consultorio(aux_c)
    assert aux_h.listaconsult[0] is not None