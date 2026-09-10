import cv2
import numpy as np

# 1. Crear el pixel BGR de prueba (Amarillo puro: B=0, G=255, R=255)
pixel = np.array([0, 255, 255], dtype=np.float32)

# Vector de pesos ajustado al orden BGR
pesos = np.array([0.114, 0.587, 0.299])

# 2. Calcular matemáticamente mediante producto punto
valor_gris = np.dot(pixel, pesos)

# 3. Imprimir el resultado
print(f"Valor matemático en escala de grises: {valor_gris:.2f}")

# 4. Verificación con OpenCV en una imagen real
# Cargar imagen real y convertir usando la función optimizada de OpenCV
imagen = cv2.imread('/workspaces/IA---2/IMAGEN/image.png')
if imagen is not None:
    img_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    print("Imagen convertida a escala de grises con éxito.")


#EJERCICIO 2

import matplotlib.pyplot as plt

# 1. Cargar la imagen en la carpeta
imagen = cv2.imread('/workspaces/IA---2/IMAGEN/image.png')  # Asegúrate de usar el nombre exacto de tu archivo

if imagen is None:
    print("Error: No se encontró la imagen. Asegúrate de haberla subido a la carpeta.")
else:
    # 2. Configurar colores para los canales en orden BGR (Azul, Verde, Rojo)
    colores = ('b', 'g', 'r')
    etiquetas = ('Canal Azul', 'Canal Verde', 'Canal Rojo')
    
    plt.figure(figsize=(10, 5))
    
    # 3. Calcular y graficar el histograma de cada canal
    for i, col in enumerate(colores):
        hist = cv2.calcHist([imagen], [i], None, [256], [0, 256])
        plt.plot(hist, color=col, label=etiquetas[i])
        plt.xlim([0, 256])

    plt.title("Histograma Comparativo de Canales RGB")
    plt.xlabel("Valor del Píxel (0 - 255)")
    plt.ylabel("Frecuencia (Cantidad de Píxeles)")
    plt.legend()
    plt.grid(True)
    
    # EN LUGAR DE plt.show(), GUARDAMOS LA IMAGEN GENERADA:
    plt.savefig('histograma_resultado.png')
    print("¡Proceso completado! La gráfica se guardó como 'histograma_resultado.png' en tu explorador de archivos.")