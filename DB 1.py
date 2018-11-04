n = int(input('Digite um número: '))
p = n % 2
if p == 0:
    print('Esse número é par.')
else:
    print('Esse número é ímpar.')
if p == 1:
    print('Esse número não é par.')
else:
    print('Esse número não é ímpar.')
if n >= 10:
    print('Esse número é maior que 10.')
else:
    print('Esse número não é maior que 10.')
d = n * 2
print('O dobro de {} é {}.'.format(n, d))
t = 0
for d in range(1, n + 1):
    if n % d == 0:
        t += 1
    else:
        t += 0
if t == 2:
    print('Esse número é primo.')
else:
    print('Esse número não é primo.')

