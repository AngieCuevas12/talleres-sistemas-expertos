import numpy as np
def funcion_escalon(z):
    if z >= 0:
        return 1
    else:
        return 0
def perceptron(X, W, b):
    Z = np.dot(X, W) + b
    salida = funcion_escalon(Z)
    return salida
pesos_and = np.array([0.5, 0.5])
sesgo_and = -0.8
print("=== Punto 2: Verificando la Compuerta AND ===")
print("Entrada [1, 1] ->", perceptron(np.array([1, 1]), pesos_and, sesgo_and))
print("Entrada [1, 0] ->", perceptron(np.array([1, 0]), pesos_and, sesgo_and))
print("Entrada [0, 1] ->", perceptron(np.array([0, 1]), pesos_and, sesgo_and))
print("Entrada [0, 0] ->", perceptron(np.array([0, 0]), pesos_and, sesgo_and))
pesos_or = np.array([0.5, 0.5])
sesgo_or = -0.4
print("\n=== Punto 3 y 4: Probando mi solucion para la Compuerta OR ===")
print("Entrada [1, 1] ->", perceptron(np.array([1, 1]), pesos_or, sesgo_or))  # deberia dar 1
print("Entrada [1, 0] ->", perceptron(np.array([1, 0]), pesos_or, sesgo_or))  # deberia dar 1
print("Entrada [0, 1] ->", perceptron(np.array([0, 1]), pesos_or, sesgo_or))  # deberia dar 1
print("Entrada [0, 0] ->", perceptron(np.array([0, 0]), pesos_or, sesgo_or))  # deberia dar 0
