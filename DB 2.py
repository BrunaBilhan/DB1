frase = str(input('Digite um texto: ')).strip().lower()
print('{} caracteres. '.format(len(frase)))
print('{} espaços. '.format(frase.count(' ')))
a = int(frase.count('a'))
e = int(frase.count('e'))
i = int(frase.count('i'))
o = int(frase.count('o'))
u = int(frase.count('u'))
v = a + e + i + o + u
if v == 1:
    print ('{} vogal.'.format(v))
else:
    print('{} vogais.'.format(v))

