frase = str(input('Digite um texto: ')).strip().lower()
print('{} caracteres. '.format(len(frase)))
print('{} espaços. '.format(frase.count(' ')))
a = int(frase.count('a'))
á = int(frase.count('á'))
à = int(frase.count('à'))
ã = int(frase.count('ã'))
e = int(frase.count('e'))
é = int(frase.count('é'))
i = int(frase.count('i'))
í = int(frase.count('í'))
o = int(frase.count('o'))
ó = int(frase.count('ó'))
õ = int(frase.count('õ'))
u = int(frase.count('u'))
ú = int(frase.count('ú'))
v = a + e + i + o + u + á + é + í + ó + ú + ã + õ + à
if v == 1:
    print ('{} vogal.'.format(v))
else:
    print('{} vogais.'.format(v))

