def calcularPuntosDelTriangulo(n):
    return int((n*(n+1))/2)

N = int(input())

i=1
    #si es para valores N muy grandes, se puede reducir con busqueda binaria
while N>calcularPuntosDelTriangulo(i):
    i+=1

if(N==calcularPuntosDelTriangulo(i)):
    print("YES")
else:
    print("NO")