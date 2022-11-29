
'''#questão1
def dobro(x):
    return(x+x)
s=dobro(5)
print(s)

'''
#questao 2
def ehper(x):
    if(x % 2 ==0):
       return ("par")
    else:
        return("não e par")
p =ehper(2)
x  =ehper(55)
print(p,x)
#quetao3
def numero_int(n):
    if( n>0):
        return("positivo")
    elif( n<0):
        return("negativo")
    else:
        return("zero")
n1=numero_int(45)
n2=numero_int(0)
n3=numero_int(-96754)
print(n1,n2,n3)
#questao4
def nome(no):
    return(no)
def hora(h):
    if( h>=0 and h<13):
        return("bom dia")
    elif( h>=13 and h<18):
        return("boa tarde")
    else:
       return("boa noite")
nome1=input("informe seu nome:")
horario=int(input("Informe o horario:"))
j=nome(nome1)
j1=hora(horario)


print(j,j1)


#questao5
def media(n1,n2,n3):
    return (n1+n2+n3)/3

aluno1 = media(3,3,10)
print(aluno1)

#6questao
def nome(n1,n2):
    if(n1<n2):
        return(n1,n2)
    else:
        return(n2,n1)
nome1=nome("Ana","Beatriz")
nome2=nome("Bento","Aline")
print(nome2)
print(nome1)
    


