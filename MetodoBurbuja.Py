def burbuja(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


numeros = [36, 67, 17, 52, 420, 69]
print(burbuja(numeros))