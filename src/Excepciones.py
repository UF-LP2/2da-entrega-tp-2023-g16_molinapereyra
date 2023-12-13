
def verifico_edad(edad):
  if edad < 100 or edad >= 0:
    return True
  else:
    return False

def verifico_dni(dni):
  if type(dni) != int or dni <= 0:
    raise Exception(f"El DNI es invalido")
  else:
    return True
  
def verifico_palabra(nombre, apellido):
  if type(nombre and apellido) == str:
    return True
  else:
    raise Exception(f"EL Nombre y/o Apellido es invalido")

def verifico_genero(genero):
  if genero == ("F" or "M"):
    return True
  else:
    return False 