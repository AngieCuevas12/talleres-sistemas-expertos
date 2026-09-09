servidor_estado = {
    "cpu_uso": 96,           
    "memoria_libre": 415,    
    "ping_respuesta": True,  
    "temperatura": 73,       
    "ventilador_activo": True 
}
def diagnosticar_servidor(hechos):
    if hechos["temperatura"] > 80 and not hechos["ventilador_activo"]:
        return """CRITICO: Sobrecalentamiento detectado
        - Temperatura: {}°C (umbral: 80°C)
        - Ventilador: APAGADO
        - Accion: Apagar servidor inmediatamente""".format(hechos["temperatura"])
    elif hechos["cpu_uso"] > 90 and not hechos["ping_respuesta"]:
        return """CRITICO: Servidor no responde con CPU sobrecargada
        - CPU: {}% (umbral: 90%)
        - Ping: FALLÓ
        - Accion: Reiniciar servidor urgente""".format(hechos["cpu_uso"])
    elif hechos["memoria_libre"] < 300 and hechos["cpu_uso"] > 70:
        return """ADVERTENCIA: Recursos del sistema bajos
        - Memoria libre: {} MB (umbral: 300 MB)
        - CPU: {}% (umbral: 70%)
        - Accion: Monitorear y considerar ampliar memoria""".format(
            hechos["memoria_libre"], hechos["cpu_uso"])
    elif hechos["temperatura"] > 70 and hechos["temperatura"] <= 80:
        return """ADVERTENCIA: Temperatura elevada
        - Temperatura: {}°C (umbral: 70-80°C)
        - Ventilador: ACTIVO
        - Accion: Verificar sistema de refrigeracion""".format(hechos["temperatura"])
    elif hechos["ping_respuesta"] and hechos["cpu_uso"] < 70 and hechos["memoria_libre"] > 500:
        return """NORMAL: Servidor funcionando correctamente
        - CPU: {}%
        - Memoria libre: {} MB
        - Ping: OK
        - Temperatura: {}°C
        - Estado: Operativo y estable""".format(
            hechos["cpu_uso"], hechos["memoria_libre"], hechos["temperatura"])
    else:
        return """ EN REVISIÓN MANUAL: Estado no determinado
        - CPU: {}%
        - Memoria libre: {} MB
        - Ping: {}
        - Temperatura: {}°C
        - Accion: Requiere inspección detallada""".format(
            hechos["cpu_uso"], hechos["memoria_libre"], 
            "OK" if hechos["ping_respuesta"] else "FALLÓ",
            hechos["temperatura"])
print("=" * 60)
print("SISTEMA DE DIAGNOSTICO DE SERVIDOR")
print("=" * 60)
print("\n--- ESCENARIO 1: Estado Normal ---")
servidor_estado = {
    "cpu_uso": 65,
    "memoria_libre": 1024,
    "ping_respuesta": True,
    "temperatura": 62,
    "ventilador_activo": True
}
print(diagnosticar_servidor(servidor_estado))
print("\n--- ESCENARIO 2: Estado Critico ---")
servidor_estado = {
    "cpu_uso": 45,
    "memoria_libre": 1024,
    "ping_respuesta": True,
    "temperatura": 85,
    "ventilador_activo": False
}
print(diagnosticar_servidor(servidor_estado))
print("\n--- ESCENARIO 3: Estado Critico ---")
servidor_estado = {
    "cpu_uso": 95,
    "memoria_libre": 256,
    "ping_respuesta": False,
    "temperatura": 60,
    "ventilador_activo": True
}
print(diagnosticar_servidor(servidor_estado))
print("\n--- ESCENARIO 4: Estado Advertencia ---")
servidor_estado = {
    "cpu_uso": 75,
    "memoria_libre": 250,
    "ping_respuesta": True,
    "temperatura": 65,
    "ventilador_activo": True
}
print(diagnosticar_servidor(servidor_estado))
print("\n--- ESCENARIO 5: Estado de Advertencia ---")
servidor_estado = {
    "cpu_uso": 68,
    "memoria_libre": 354,
    "ping_respuesta": True,
    "temperatura": 77,
    "ventilador_activo": True
}
print(diagnosticar_servidor(servidor_estado))