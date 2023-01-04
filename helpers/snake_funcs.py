def convertir_a_snake_case(cadena):
    resultado = ""
    ultimo_era_mayuscula = False
    for i, caracter in enumerate(cadena):
        if caracter.isupper():
            if ultimo_era_mayuscula:
                resultado += caracter.lower()
            else:
                if i > 0:
                    resultado += "_" + caracter.lower()
                else:
                    resultado += caracter.lower()
            ultimo_era_mayuscula = True
        else:
            resultado += caracter
            ultimo_era_mayuscula = False
    return resultado