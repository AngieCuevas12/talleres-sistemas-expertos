import numpy as np
from sklearn.neighbors import KNeighborsClassifier
#amplio con mas fila una columna 
X_entrenamiento = np.array([
    [20, 30, 0],  
    [40, 50, 2],   
    [35, 45, 1],   
    [23, 25, 0],
    [43, 50, 3],
    [28, 44, 2],
    [34, 32, 1],
    [54, 62, 3],
    [38, 35, 1],
    [48, 53, 2],
])
#actualizo para que coincida 
Y_entrenamiento = np.array([0, 1, 1, 0, 1, 1, 0, 1, 0, 1])
#pongo cliente nuevo 
nuevo_cliente = np.array([[30, 40, 1]])  
#creo el modelo knn y que mire a un vecino mas cercano 
modelo_knn_k1 = KNeighborsClassifier(n_neighbors=1)
#memoriza todos los datos que le di en x y y
modelo_knn_k1.fit(X_entrenamiento, Y_entrenamiento)
#predigo la clase nueva del cliente nuevo
prediccion_k1 = modelo_knn_k1.predict(nuevo_cliente)
print("Prediccion con K=1")
print("Clase predicha:", prediccion_k1[0])
#creo un nuevo modelo pero esta vez cambio el 1 al 5 para comparar si cambia el valor de k el cual hara que el resultadoo cambie
modelo_knn_k5 = KNeighborsClassifier(n_neighbors=5)
modelo_knn_k5.fit(X_entrenamiento, Y_entrenamiento)
prediccion_k5 = modelo_knn_k5.predict(nuevo_cliente)
print("Prediccion con K=5")
print("Clase predicha:", prediccion_k5[0])

