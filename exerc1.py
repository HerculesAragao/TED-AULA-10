vetor=[]
x=0
while x<20:
    numero = input('Digite o %dº. número: ' % (x+1))
    x=x+1
    vetor.append(numero)
x=0
while x<20:
    print(vetor[19-x])
    x=x+1