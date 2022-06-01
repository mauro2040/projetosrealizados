p1=0
n1=0
cont = 0
resp="S"
media=soma=0

while resp in "Ss":
    n1=int(input("Informe um numero"))
    resp=str(input("Quer continuar")).upper().strip()[0]
    soma = (soma+n1)
    cont = cont +1
    media= (soma/cont)
    if cont == 1:
        maior=menor=n1
    else:
        if n1> maior:
            maior = n1
        if n1<menor:
            menor = n1

    if resp == "N":
        print("A media fo {}".format(media))
        print("A soma foi {}".format(soma))
        print("O maior numero foi {}, e o menor foi {}".format(maior,menor))
print("Finalizado")