# import itertools as it

anagrama = input('Digite 1 palavra : ')
a = sorted(anagrama)
t = len(a) # Só para gerar de acordo com numero de caracteres digitado para contagem no FOR
# s = list(it.combinations(anagrama, 2))
# s1 = ''.join(anagrama)
# l = list(zip(it.count(), anagrama))

for i in range(t):
    # print(f'Valor do i = {a[i] + a[i-1] + a[i-2]}')
    if a[i] == a[i-1]:
        print(f'Encontrado anagramas dentro da palavra {anagrama}. A lista de todos os anagramas pares são:[{a[i]},{a[i-1]}] que estão nas posições: : [{anagrama.index(a[i])}, {anagrama.index(a[i-1])}]')
    if  a[i] + a[i-1] + a[i-2] in anagrama:
        print(f'A lista de todos os anagramas de 3 letras são: [{a[i]} , {a[i-1]} , {a[i-2]}] que estão nas posições : [{anagrama.index(a[i])}, {anagrama.index(a[i-1])}, {anagrama.index(a[i-2])}]')
