import ply.yacc as yacc
from lexer import lexer, tokens


# Definición de las funciones asociadas con las reglas de producción
def p_inicio(p):
    "inicio : objeto"
    # p[1] = resultado de 'objeto'
    p[0] = p[1]   # El valor de la entrada completa es el dict devuelto por objeto

def p_objeto(p):
    "objeto : LBRACE miembros RBRACE"
    p[0] = p[2]

#Miembros
def p_miembros_uno(p):
    "miembros : par"
    # p[1] = resultado de 'par' → tupla (clave, valor)
    clave, valor = p[1]
    p[0] = {clave: valor}  # members devuelve un dict con un par

def p_miembros_varios(p):
    "miembros : miembros COMMA par"
    # p[1] = dict previo, p[2] = token ',', p[3] = (clave, valor)
    d = p[1] #
    clave, valor = p[3] #par
    d[clave] = valor    # sobrescribir clave
    p[0] = d

#Par
def p_par(p):
    "par : STRING COLON valor"
    # p[1] = STRING (sin comillas si el lexer lo limpió), p[2] = ':', p[3] = valor (str/int/dict)
    p[0] = (p[1], p[3])  # devolver la pareja clave-valor como tupla


#Valores
def p_valor_string(p):
    "valor : STRING"
    # p[1] = cadena limpia
    p[0] = p[1]

def p_valor_number(p):
    "valor : NUMBER"
    # p[1] = int (si en lexer convertiste)
    p[0] = p[1]

def p_valor_objeto(p):
    "valor : objeto"
    # p[1] = dict retornado por objeto
    p[0] = p[1]


#Manejar errores
def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")  # Imprime el token donde ocurrió el error
    else:
        print("Syntax error at EOF")  # Indica un error al final de la entrada

# Construccion analizador sintactico
parser = yacc.yacc() #se crea instancia del analizador sintáctico
