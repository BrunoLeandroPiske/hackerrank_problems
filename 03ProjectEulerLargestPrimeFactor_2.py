#achar o maior fator do numero
t = int(input())

for z in range(t):
    N = int(input())
    i = 2
    largest_prime = 2
    while i*i <= N:
        while N % i == 0:
            largest_prime = i
            N //= i
        i += 1
        if N>largest_prime:
            largest_prime = N;
    print(largest_prime)
