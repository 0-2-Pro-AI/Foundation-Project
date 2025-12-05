tuplo = (2,4,23,76,3)

def maior_elemento (x):
    return max (x)

maior_elemento((2,4,23,76,3))

def mairor_elemento(x):
    maior = x[0]

    for elemento in x:
        if elemento > maior:
            maior = elemento 
    
        return maior
         
def menor_elemento(y):
    menor_elemento((3,4,5,6,7),5)
    menor_elemento((3,4,5,6,7),2)
    
    menor= y[0]
    for elemento in y:
        if elemento< menor:
            menor = elemento

        return menor
    

