def valid_pass(password: str):
    errores = []
    if not validar_longitud(password):
        errores.append('La password debe contener al menos 8 caracteres')
    if not validar_dos_numeros(password):
        errores.append('La password debe contener al menos 2 números')
    if not validar_mayusculas(password):
        errores.append('La password debe contener al menos una letra mayúscula')
    if not validar_caracter_especial(password):
        errores.append('La password debe contener al menos un caracter especial')

    if len(errores) > 0:
        return False, '\n'.join(errores)
    return True


def validar_longitud(password):
    if len(password) >= 8:
        return True
    return False


def validar_dos_numeros(password):
    cont = 0
    for letra in password:
        if letra.isdigit():
            cont += 1

        if cont >= 2:
            return True

    return False


def validar_mayusculas(password):
    for letra in password:
        if letra.isupper():
            return True

    return False


def validar_caracter_especial(password):
    for letra in password:
        if not letra.isalnum():
            return True

    return False
