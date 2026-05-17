import random


def busqueda_binaria_conteo(arr: list[int], objetivo: int,
                           lo: int, hi: int,
                           conteo: list[int]) -> int:
   """
   Igual que busqueda_binaria, pero incrementa conteo[0]
   en cada comparación con arr[mid].
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
# Generando un arreglo aleatorio dependiendo de su longitud
n=1048576 #Longitud del arreglo
A = [random.randint(1, 100000000) for _ in range(n)]


#Ordenando el arreglo generado para aplicar búsqueda binaria
'''
USAR SOLO SI N=1024 para 1048576 mejor ignorar esta parte del codigo porfavor.
def ordenamiento_burbuja(A):
   n=len(A)
   for i in range(n):
       # Bandera para optimizar y detener el ciclo si ya está ordenada
       intercambiado = False
      
       # El último elemento i ya está ordenado en cada pasada
       for j in range(0, n - i - 1):
           if A[j] > A[j + 1]:
               # Intercambio de elementos
               A[j], A[j + 1] = A[j + 1], A[j]
               intercambiado = True
              
       # Si no hubo intercambios en esta pasada, la lista ya está ordenada
       if not intercambiado:
           break
   return A
   '''
A.sort()
medio=len(A)//2
mejor = A[(0 + len(A) - 1) // 2]
peor=10000000000000000000
print(f"\nBuscando el elemento {peor}")
mis_comparaciones = [0] # Creamos la lista con un cero
indice = busqueda_binaria_conteo(A,peor, 0, len(A)-1, mis_comparaciones)
print(f"Encontrado en índice: {indice}")
print(f"Comparaciones totales: {mis_comparaciones[0]}")
