import ply.lex as lex
import re

# Tokens
tokens = (
    'LBRACE',       # {
    'RBRACE',       # }
    'COLON',        # :
    'COMMA',        # ,
    'STRING',       # "ejemplo" 
    'NUMBER',       # 123
)

#Reglas de expresion regular para cada token
def t_LBRACE(t):
    r'\{'
    print(f"→ Reconocí un LBRACE: {{")
    return t

def t_RBRACE(t):
    r'\}'
    print(f"→ Reconocí un RBRACE: }}")
    return t

def t_COLON(t):
    r':'
    print(f"→ Reconocí un COLON: :")
    return t

def t_COMMA(t):
    r','
    print(f"→ Reconocí un COMMA: ,")
    return t

def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value.strip('"') # Quitamos comillas
    print(f"→ Reconocí un STRING: {t.value}")
    return t

def t_NUMBER(t):
    r'\d+' #
    t.value = int(t.value) # Convertimos a int
    print(f"→ Reconocí un NUMBER: {t.value}")
    return t

# Caracteres que vamos a ignorar (tabulares, espacios, saltos de linea)
t_ignore = ' \t\n'

# Caracteres ilegales
def t_error(t):
    print(f" ERROR: Carácter '{t.value[0]}' no válido")  # Imprime el carácter ilegal
    t.lexer.skip(1)  # Salta el carácter ilegal

# Lexer
lexer = lex.lex() # Se crea instancia del analizador léxico
