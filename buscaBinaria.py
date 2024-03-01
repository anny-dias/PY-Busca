#Busca Binária

def busca_binaria(array, x, low, high):
    while low <= high:
        mid = (high + low) // 2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
        return -1
    
array = [3, 4, 5, 6, 7, 8, 9]
x = 6
resultado = busca_binaria(array, x, 0, len(array) -1)
if resultado != -1:
    print("Elemento está presente no index " + str(resultado))
else:
    print("Elemento não encontrado")
