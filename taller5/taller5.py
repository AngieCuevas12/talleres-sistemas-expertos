import numpy as np
import skfuzzy as fuzz
#librerias que utilice 
def centroide(x, curva):
    x = np.array(x)
    curva = np.array(curva)
#formulas 
    numerador = np.sum(x * curva)   
    denominador = np.sum(curva)     
    return numerador / denominador
#estos son los datos 
x_descuento = [10, 20, 30, 40]
mu_descuento = [0.2, 0.8, 0.8, 0.0]
resultado_descuento = centroide(x_descuento, mu_descuento)
print("Validacion: ")
print(f"Descuento exacto: {resultado_descuento:.2f}%")
# esto crea 100 numeros repartidos parejo entre 0 y 100
x_frenado = np.linspace(0, 100, 100)  
media = 70
sigma = 9  
curva_frenado = fuzz.gaussmf(x_frenado, media, sigma)
# aqui uso mi propia funcion centroide
fuerza_frenado_crisp = centroide(x_frenado, curva_frenado)
print(" Defuzzificacion del sistema de frenado:")
print(f"Fuerza de frenado exacta calculada: {fuerza_frenado_crisp:.2f} Newtons")
#Comparo mi resultado con el de la libreria
fuerza_con_libreria = fuzz.defuzz(x_frenado, curva_frenado, 'centroid')
print(f"Fuerza calculada con skfuzzy: {fuerza_con_libreria:.2f} Newtons")