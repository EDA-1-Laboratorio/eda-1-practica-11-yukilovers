def busqueda_binaria_conteo(arr: list[int], objetivo: int,
                           lo: int, hi: int,
                           conteo: list[int]) -> int:
   """
   Busca 'objetivo' en arr[lo..hi] (extremos inclusivos).


   Precondición: arr está ordenado de menor a mayor.
   Retorna el índice de 'objetivo' si existe, o -1 si no está.
   """


   # Paso base
   if lo > hi:
       return -1


   mid = (lo + hi) // 2


   # --- Primera comparación ---
   conteo[0] += 1
   if arr[mid] == objetivo:
       return mid


   # --- Segunda comparación ---
   conteo[0] += 1
   if objetivo < arr[mid]:
       return busqueda_binaria_conteo(arr, objetivo, lo, mid - 1, conteo)
   else:
       return busqueda_binaria_conteo(arr, objetivo, mid + 1, hi, conteo)


# --- Cómo se usa ---
A = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
print("\nBuscando el 23.")
mis_comparaciones = [0] # Creamos la lista con un cero
indice = busqueda_binaria_conteo(A, 23, 0, len(A)-1, mis_comparaciones)
print(f"Encontrado en índice: {indice}")
print(f"Comparaciones totales: {mis_comparaciones[0]}")


print("\nBuscando el 16.")
mis_comparaciones = [0] # Creamos la lista con un cero
indice = busqueda_binaria_conteo(A, 16, 0, len(A)-1, mis_comparaciones)
print(f"Encontrado en índice: {indice}")
print(f"Comparaciones totales: {mis_comparaciones[0]}")


print("\nBuscando el 2.")
mis_comparaciones = [0] # Creamos la lista con un cero
indice = busqueda_binaria_conteo(A, 2, 0, len(A)-1, mis_comparaciones)
print(f"Encontrado en índice: {indice}")
print(f"Comparaciones totales: {mis_comparaciones[0]}")


print("\nBuscando el 91.")
mis_comparaciones = [0] # Creamos la lista con un cero
indice = busqueda_binaria_conteo(A, 91, 0, len(A)-1, mis_comparaciones)
print(f"Encontrado en índice: {indice}")
print(f"Comparaciones totales: {mis_comparaciones[0]}")


print("\nBuscando el 99.")
mis_comparaciones = [0] # Creamos la lista con un cero
indice = busqueda_binaria_conteo(A, 99, 0, len(A)-1, mis_comparaciones)
print(f"Encontrado en índice: {indice}")
print(f"Comparaciones totales: {mis_comparaciones[0]}")


print("\nBuscando el 1.")
mis_comparaciones = [0] # Creamos la lista con un cero
indice = busqueda_binaria_conteo(A, 1, 0, len(A)-1, mis_comparaciones)
print(f"Encontrado en índice: {indice}")
print(f"Comparaciones totales: {mis_comparaciones[0]}")


print("\nBuscando el 5.")
mis_comparaciones = [0] # Creamos la lista con un cero
indice = busqueda_binaria_conteo(A, 5, 0, len(A)-1, mis_comparaciones)
print(f"Encontrado en índice: {indice}")
print(f"Comparaciones totales: {mis_comparaciones[0]}")
