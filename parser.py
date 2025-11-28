import ply.yacc as yacc
from lexer import lexer, tokens


# Definición de las funciones asociadas con las reglas de producción
# --- REGLA INICIAL ---
def p_inicio(p):
    '''inicio : objeto'''
    p[0] = p[1]

# --- ESTRUCTURA DE OBJETOS { } ---
def p_objeto(p):
    '''objeto : LBRACE miembros RBRACE
              | LBRACE RBRACE'''
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = {}

def p_miembros(p):
    '''miembros : par
                | miembros COMMA par'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[1].update(p[3])
        p[0] = p[1]

# --- PAR CLAVE: VALOR ---
def p_par(p):
    '''par : clave COLON valor'''
    p[0] = {p[1]: p[3]}

# Esta regla permite que las palabras reservadas funcionen como claves
def p_clave(p):
    '''clave : FOLIO
             | FECHA_TOMA
             | FECHA_VALIDACION
             | PACIENTE
             | NOMBRE
             | FECHA_NAC
             | SEXO
             | EDAD
             | MEDICO
             | SECCION
             | PARAMETROS
             | RESULTADO
             | UNIDAD
             | LIMITE
             | FIRMA
             | RESPONSABLE
             | CEDULA
             | STRING'''  
    p[0] = p[1]

# --- ESTRUCTURA DE LISTAS [ ] ---
def p_lista(p):
    '''lista : LBRACKET elementos RBRACKET
             | LBRACKET RBRACKET'''
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = []

def p_elementos(p):
    '''elementos : valor
                 | elementos COMMA valor'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[3])
        p[0] = p[1]

# --- VALORES POSIBLES ---
def p_valor(p):
    '''valor : STRING
             | NUMBER
             | FECHA
             | FECHA_HORA
             | CARACTER
             | objeto
             | lista'''
    p[0] = p[1]

#Manejar errores
def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")  # Imprime el token donde ocurrió el error
    else:
        print("Syntax error at EOF")  # Indica un error al final de la entrada

# Construccion analizador sintactico
parser = yacc.yacc() #se crea instancia del analizador sintáctico
