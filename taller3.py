import cv2
import numpy as np

# 1. Cargar una imagen en escala de grises
imagen = cv2.imread('/workspaces/IA---2/imagen2/image.png', cv2.IMREAD_GRAYSCALE)

# Verificar que la imagen se haya cargado correctamente
if imagen is None:
    print("Error: No se encontró la imagen. Verifica la ruta ingresada.")
else:
    # 2. Binarización estática con umbral
    _, imagen_binaria = cv2.threshold(imagen, 127, 255, cv2.THRESH_BINARY)

    # 3. Construir Elemento Estructurante (Kernel de 3x3)
    kernel = np.ones((3, 3), np.uint8)

    # 4. Operación Morfológica de APERTURA (Erosión seguida de Dilatación)
    imagen_apertura = cv2.morphologyEx(imagen_binaria, cv2.MORPH_OPEN, kernel)

    # 5. Operación Morfológica de CIERRE (Dilatación seguida de Erosión)
    imagen_cierre = cv2.morphologyEx(imagen_binaria, cv2.MORPH_CLOSE, kernel)

    # 6. Guardar los resultados como archivos de imagen en lugar de usar cv2.imshow
    cv2.imwrite('/workspaces/IA---2/1_binaria.png', imagen_binaria)
    cv2.imwrite('/workspaces/IA---2/2_apertura.png', imagen_apertura)
    cv2.imwrite('/workspaces/IA---2/3_cierre.png', imagen_cierre)

    print("Procesamiento completado con éxito. Se crearon los archivos '1_binaria.png', '2_apertura.png' y '3_cierre.png'.")