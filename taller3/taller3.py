def membresia_triangular(x, a, b, c):
    if x <= a or x >= c:
        return 0.0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x < c:
        return (c - x) / (c - b)
conjuntos = {
    "Novato": {"a": 0, "b": 0, "c": 5},
    "Intermedio": {"a": 2, "b": 5, "c": 8},
    "Experto": {"a": 5, "b": 10, "c": 20}
}
conductores = [3, 6, 12]  
print("=" * 70)
print("SISTEMA DE EVALUACION DIFUSA - EXPERIENCIA DE CONDUCTOR")
print("=" * 70)
for experiencia in conductores:
    print(f"\n--- Conductor con {experiencia} años de experiencia ---")
    grados = {}
    for nombre, params in conjuntos.items():
        grado = membresia_triangular(experiencia, params["a"], params["b"], params["c"])
        grados[nombre] = grado
        print(f" Pertenencia a '{nombre}': {grado*100:.1f}%")
    mejor_categoria = max(grados, key=grados.get)
    mejor_grado = grados[mejor_categoria]
    print(f" Mejor categoría: {mejor_categoria} (μ = {mejor_grado*100:.1f}%)")
    print("  " + "-" * 40)
print("\n" + "=" * 70)
print("RESUMEN DE CLASIFICACION:")
print("=" * 70)
print(f"  • Conductor con 3 años → Novato")
print(f"  • Conductor con 6 años → Intermedio")
print(f"  • Conductor con 12 años → Experto")
print("=" * 70)