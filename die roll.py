resultadosPosibles= ["","1/1","5/6","2/3","1/2","1/3","1/6"]
Y,W=map(int,input().split())

mayorPuntaje= Y if Y>W else W

print( resultadosPosibles[mayorPuntaje] )