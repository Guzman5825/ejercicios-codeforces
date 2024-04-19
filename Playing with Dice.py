a,b=map(int, input().split() )
casosFavorablesParaA=0
casosFavorablesParaB=0
empates=0

#primero caso ambos dados son iguales
if a==b:
    print("0 6 0")

# 'a' es menor a 'b' entonces a esta mas cerca del 1
if a<b:
    m=(a+b)//2  #m:valor entero medio entre a y b
    if (a+b)%2==0:   #eso significa que dio un medio sin decimales
        casosFavorablesParaA=m-1
        empates=1
    else:
        casosFavorablesParaA=m
        empates=0
    print(casosFavorablesParaA,end=" ")
    print(empates,end=" ")
    print(6-casosFavorablesParaA-empates)#el resto de casos para B
if a>b:   #entonces 'b' esta mas cerca al 1 
    m=(a+b)//2  
    if (a+b)%2==0:   
        casosFavorablesParaB=m-1
        empates=1
    else:
        casosFavorablesParaB=m
        empates=0
    print(6-casosFavorablesParaB-empates,end=" ")#el resto de casos para B
    print(empates,end=" ")
    print(casosFavorablesParaB)

    
    