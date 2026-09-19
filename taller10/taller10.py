import numpy as np
# Funcion de Activacion: Sigmoide (aplasta cualquier numero para que quede entre 0 y 1, como si fuera una probabilidad
def sigmoide(x):
    return 1 / (1 + np.exp(-x))
X = np.array([0.5, 0.8, 0.2])
# Matriz W1 de 3 entradas x 4 neuronas
W1 = np.array([
    [0.1,  0.2, -0.3,  0.4],
    [-0.5, 0.6,  0.7, -0.8],
    [0.9, -0.1,  0.2,  0.3]
])
b1 = np.array([0.1, -0.2, 0.3, -0.4]) 
Z1 = np.dot(X, W1) + b1
A1 = sigmoide(Z1)
W2 = np.array([0.5, -0.6, 0.7, 0.8])
b2 = np.array([-0.1])
Z2 = np.dot(A1, W2) + b2
Salida_Final = sigmoide(Z2)

print("Punto 1: Prediccion con 1 cliente")
print("Prediccion de la Red (Probabilidad):", np.round(Salida_Final[0], 4))
print("\n=== Punto 2: Analizando Z1 y A1 ===")
print("Z1 (valores puros, antes de la sigmoide):", Z1)
print("A1 (despues de pasar por la sigmoide):", A1)
# Ahora cambio X para que sea una matriz de 2x3 2 clientes, cada unocon 3 caracteristicas
X_lote = np.array([
    [0.5, 0.8, 0.2],   
    [0.1, 0.9, 0.9]    
])
Z1_lote = np.dot(X_lote, W1) + b1
A1_lote = sigmoide(Z1_lote)
Z2_lote = np.dot(A1_lote, W2) + b2
Salida_lote = sigmoide(Z2_lote)

print("Punto 3 y 4: Procesando 2 clientes en lote (batch)")
print("Z1 del lote (una fila por cliente):")
print(Z1_lote)
print("A1 del lote (despues de la sigmoide):")
print(A1_lote)
print("Prediccion final para los 2 clientes:")
print(np.round(Salida_lote, 4))