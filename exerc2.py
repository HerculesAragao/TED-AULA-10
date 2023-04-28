vet=[1,2,3,3,4,5,6,7,7,8]
numeros=[]
num_repetidos=set()
for num in vet:
    if num not in numeros:
        numeros.append(num)
    else:
        num_repetidos.add(num)
print(f'Vetor VET= {vet}')
print(f'Numeros= {numeros}')
print(f'Num. Repetidos= {num_repetidos}')