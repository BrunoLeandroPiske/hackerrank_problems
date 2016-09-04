N = int(input())
lista = []
for i in range(N):
   lista.append(input())
resultado = 0
for i in range(len(lista)):
   resultado += int(lista[i])
print(str(resultado)[:10])
