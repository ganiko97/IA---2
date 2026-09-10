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