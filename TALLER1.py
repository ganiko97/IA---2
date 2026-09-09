import numpy as np

# 1. Crear matriz de prueba 5x5 con valores sobreexpuestos (entre 200 y 255)
matriz_original = np.random.randint(200, 255, (5, 5))

# Parámetros solicitados:
# Reducción de contraste del 50% -> alpha = 0.5
# Disminución de brillo en 50 unidades -> beta = -50
alpha = 0.5
beta = -50.0

# 2. Aplicar la transformación matemática: A_nueva = (alpha * A) + beta
matriz_transformada = (alpha * matriz_original) + beta

# 3. Asegurar límites de 0 a 255 y convertir a tipo de dato uint8
matriz_procesada = np.clip(matriz_transformada, 0, 255).astype(np.uint8)

# 4. Imprimir ambas matrices para comparar
print("=== MATRIZ ORIGINAL (SOBREEXPUESTA) ===")
print(matriz_original)

print("\n=== MATRIZ PROCESADA (AJUSTADA) ===")
print(matriz_procesada)


# ==========================================
# LABORATORIO FINAL: PROGRAMANDO UN KERNEL
# (Convolución / Filtro 3x3)
# ==========================================

print("\n" + "="*40)
print("=== TALLER DE LABORATORIO FINAL ===")

# 1. Crear en NumPy las matrices "Sección de Imagen (I)" y "Kernel (K)"
I = np.array([
    [100, 100, 100],
    [100, 200, 100],
    [100, 100, 100]
])

K = np.array([
    [ 0, -1,  0],
    [-1,  5, -1],
    [ 0, -1,  0]
])

# 2. Calcular el valor central (Producto Hadamard e/ elemento y suma total)
producto_hadamard = I * K
pixel_central = np.sum(producto_hadamard)

# 3. Imprimir el resultado del píxel central
print(f"\nValor del píxel central calculado: {pixel_central}")