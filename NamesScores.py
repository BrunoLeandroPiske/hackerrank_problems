alfabeto = ["a", "b", "c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
names = []
N = int(input())
for i in range(N):
    names.append(input())
calc_names = []
N = int(input())
for i in range(N):
    calc_names.append(input())
names.sort()
for i in range(len(calc_names)):
    name = calc_names[i]
    soma = 0
    for e in range(len(name)):
        posicao = alfabeto.index(name[e].lower())+1
        soma += posicao
    total = soma * (names.index(name)+1)
    print(total)
