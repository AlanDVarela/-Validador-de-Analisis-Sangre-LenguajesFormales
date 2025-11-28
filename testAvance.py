from lexer import lexer
from parser import parser

#prueba a realizar
data2 = '''{
      "folio": 15502427,
      "fecha_toma": "14/06/2020 07:51:57",
      "fecha_validacion": "14/06/2020 17:08:05",
      "paciente": {
        "nombre": "Ramírez Guzmán, María",
        "fecha_nacimiento": "25/04/1985",
        "sexo": "F",
        "edad": 35
      }
    }''' # cadena de entrada

data = '''{
    "folio": "15502427",
    "fecha_toma": "14/06/2020 07:51:57",
    "paciente": {
        "nombre": "Juan Perez",
        "fecha_nacimiento": "25/04/1985",
        "sexo": "M",
        "edad": 35
    },
    "parametros": [
        {
            "nombre": "Leucocitos",
            "resultado": 5.9
        }
    ]
}'''



lexer.input(data) # Se analiza la cadena por el analizador léxico
print(f"Analizando fragmento:\n {data} \n")
print("=== ANALIZADOR LÉXICO ===")
for token in lexer:
    print(f"Token: {token.type}, Valor: {token.value}")

# se analiza la cadena por el parser sintáctico
print("\n=== ANALIZADOR SINTÁCTICO ===\n")
result = parser.parse(data) 
print("\nResultado del análisis sintáctico:\n")
if result is None:
    print("\nArchivo no válido")
else:
    print("\nArchivo válido:\n")
    print(result)