import numpy as np
from sklearn.svm import SVC
X = np.array([[2, 2], [3, 3], [4, 2], [6, 6], [7, 8], [8, 7]])
Y = np.array([0, 0, 0, 1, 1, 1])  
modelo_svm = SVC(kernel='linear')
modelo_svm.fit(X, Y)
vectores = modelo_svm.support_vectors_
print("Punto 1: vectores de Soporte (kernel lineal)")
print(vectores)
nuevo_punto = np.array([[5, 4]])
pred = modelo_svm.predict(nuevo_punto)
print("El punto [5,4] pertenece a la clase:", pred[0])
X_confuso = np.array([[2, 2], [3, 3], [4, 2], [6, 6], [7, 8], [8, 7], [5, 5]])
Y_confuso = np.array([0, 0, 0, 1, 1, 1, 0])  

modelo_svm_lineal_confuso = SVC(kernel='linear')
modelo_svm_lineal_confuso.fit(X_confuso, Y_confuso)

print("Punto 3: reentrenando el modelo lineal con el punto que confunde")
print("Vectores de Soporte:", modelo_svm_lineal_confuso.support_vectors_)
pred_confuso_lineal = modelo_svm_lineal_confuso.predict(nuevo_punto)
print("El punto [5,4] ahora pertenece a la clase:", pred_confuso_lineal[0])

modelo_svm_rbf = SVC(kernel='rbf')
modelo_svm_rbf.fit(X_confuso, Y_confuso)

print("Punto 4: mismo dataset confuso pero con kernel rbf")
print("Vectores de Soporte:", modelo_svm_rbf.support_vectors_)
pred_confuso_rbf = modelo_svm_rbf.predict(nuevo_punto)
print("El punto [5,4] con RBF pertenece a la clase:", pred_confuso_rbf[0])

