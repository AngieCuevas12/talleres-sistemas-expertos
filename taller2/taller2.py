hechos = {
    "monto_transaccion": 235000,
    "pais_extranjero": True,
    "usuario_verificado": False,
    "dispositivo_confiable": False,
    "intentos_fallidos": 2
}
reglas = [
    {
        "id": "R1",
        "condiciones": {"monto_transaccion": lambda x: x > 5000},
        "conclusion": {"transaccion_inusual": True}
    },
    {
        "id": "R2",
        "condiciones": {"transaccion_inusual": True, "pais_extranjero": True},
        "conclusion": {"bloquear_tarjeta": True}
    },
    {
        "id": "R3",
        "condiciones": {"intentos_fallidos": lambda x: x >= 3},
        "conclusion": {"cuenta_sospechosa": True}
    },
    {
        "id": "R4",
        "condiciones": {"cuenta_sospechosa": True, "dispositivo_confiable": False},
        "conclusion": {"bloquear_tarjeta": True}
    },
    {
        "id": "R5",
        "condiciones": {"bloquear_tarjeta": True},
        "conclusion": {"enviar_alerta": True}
    },
    {
        "id": "R6",
        "condiciones": {"monto_transaccion": lambda x: x > 10000, "usuario_verificado": False},
        "conclusion": {"requerir_autenticacion": True}
    }
]
def motor_forward_chaining(hechos_iniciales, reglas):
    hechos = hechos_iniciales.copy()
    nuevos_hechos = True
    ciclo = 0
    print("=" * 70)
    print("MOTOR DE INFERENCIA - DETECCION DE FRAUDE")
    print("=" * 70)
    print(f"Hechos iniciales: {hechos_iniciales}\n")
    while nuevos_hechos:
        ciclo += 1
        nuevos_hechos = False
        print(f"--- CICLO {ciclo} ---")
        for regla in reglas:
            condiciones_cumplidas = True
            for clave, valor in regla["condiciones"].items():
                if callable(valor):  
                    if clave not in hechos or not valor(hechos[clave]):
                        condiciones_cumplidas = False
                        break
                else:  
                    if hechos.get(clave) != valor:
                        condiciones_cumplidas = False
                        break
            if condiciones_cumplidas:
                for clave, valor in regla["conclusion"].items():
                    if clave not in hechos: 
                        hechos[clave] = valor
                        nuevos_hechos = True
                        print(f" Disparando {regla['id']} -> {clave} = {valor}")
                    elif hechos[clave] != valor: 
                        hechos[clave] = valor
                        nuevos_hechos = True
                        print(f"Disparando {regla['id']} -> {clave} actualizado a {valor}")
        if not nuevos_hechos:
            print(" No se dispararon nuevas reglas\n")
        else:
            print(f" Hechos actuales: {hechos}\n")
    return hechos
print("\n" + "=" * 70)
print("EJECUTANDO SISTEMA DE DETECCION DE FRAUDE")
print("=" * 70)
resultado_final = motor_forward_chaining(hechos, reglas)
print("\n" + "=" * 70)
print("RESULTADO FINAL:")
print("=" * 70)
for clave, valor in resultado_final.items():
    print(f"  {clave}: {valor}")
if resultado_final.get("bloquear_tarjeta", False):
    print("\n ALERTA: Se ha bloqueado la tarjeta por fraude")
else:
    print("\nTransacción segura - No se detectaron anomalías")

if resultado_final.get("enviar_alerta", False):
    print("Alerta de seguridad enviada al equipo de fraude")
print("=" * 70)
print("\n\n" + "=" * 70)
print("ESCENARIOS DE PRUEBA")
print("=" * 70)
print("\n--- ESCENARIO 1: Transaccion normal ---")
hechos_test = {
    "monto_transaccion": 500,
    "pais_extranjero": False,
    "usuario_verificado": True,
    "dispositivo_confiable": True,
    "intentos_fallidos": 0
}
resultado = motor_forward_chaining(hechos_test, reglas)
print(f"Decisión: {' BLOQUEADO' if resultado.get('bloquear_tarjeta', False) else ' APROBADO'}")
print("\n--- ESCENARIO 2: Transaccion inusual en pais extranjero ---")
hechos_test = {
    "monto_transaccion": 7500,
    "pais_extranjero": True,
    "usuario_verificado": True,
    "dispositivo_confiable": True,
    "intentos_fallidos": 0
}
resultado = motor_forward_chaining(hechos_test, reglas)
print(f"Decisión: {' BLOQUEADO' if resultado.get('bloquear_tarjeta', False) else 'APROBADO'}")
print("\n--- ESCENARIO 3: Multiples intentos fallidos ---")
hechos_test = {
    "monto_transaccion": 1000,
    "pais_extranjero": False,
    "usuario_verificado": False,
    "dispositivo_confiable": False,
    "intentos_fallidos": 3
}
resultado = motor_forward_chaining(hechos_test, reglas)
print(f"Decisión: {' BLOQUEADO' if resultado.get('bloquear_tarjeta', False) else ' APROBADO'}")