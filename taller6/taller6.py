from sklearn.tree import DecisionTreeClassifier, export_text
import numpy as np
#librerias que utilice 
# creacion de columnass
X = np.array([
    [25, 9, 2],   
    [23, 5, 3],
    [18, 8, 1],
    [45, 1, 0],   
    [50, 2, 2],
    [38, 2, 0],
    [20, 4, 4],
    [62, 1, 1],
    [27, 4, 2],
    [56, 0, 0],
])
# aqui pongo si cada cliente dio clic o no en el mismo orden que las filas de X
Y = np.array([1, 1, 1, 0, 0, 0, 1, 0, 1, 0])
#creo el modelo arbbol
arbol = DecisionTreeClassifier(max_depth=3, random_state=0)
#revisa los datos de X y Y 
arbol.fit(X, Y)
nombres_variables = ["Edad", "Horas_Online", "Compras_Previas"]
#puse esta funcion que convierte el arbol en texto 
reglas_texto = export_text(arbol, feature_names=nombres_variables)
print("Base de Reglas generada automaticamente por la IA:\n")
print(reglas_texto)
