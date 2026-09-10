#se define los diferentes valores 
desempeño_pobre = 0.1
desempeño_promedio = 0.10
desempeño_excelente = 0.95
antiguedad_corta = 0.5
antiguedad_larga = 0.9 
def motor_bonos(desempeño_pobre, desempeño_promedio, desempeño_excelente,
                 antiguedad_corta, antiguedad_larga):
#se evalua las 3 reglas
    bono_bajo = max(desempeño_pobre, antiguedad_corta)
    bono_medio = desempeño_promedio
    bono_alto = min(desempeño_excelente, antiguedad_larga)
#se retorna un dicionario con los 3 resltados 
    return {
        "BONO_BAJO": bono_bajo,
        "BONO_MEDIO": bono_medio,
        "BONO_ALTO": bono_alto
    }
# llamo la funcion con los datos para ver resultado
resultado = motor_bonos(
    desempeño_pobre, desempeño_promedio, desempeño_excelente,
    antiguedad_corta, antiguedad_larga
)
print("Fuerza de activacion")
for conclusion, fuerza in resultado.items():
    print(f"{conclusion}: {fuerza}")
fuerza_regla_A = 0.4  
fuerza_regla_B = 0.7  
#junto las dos reglas usando el valor mas alto de las dos
bono_alto_final = max(fuerza_regla_A, fuerza_regla_B)
print("Agregacion de 'Bono Alto': ")
print(f"Fuerza final de Bono Alto (tras agregar con MAX): {bono_alto_final}")