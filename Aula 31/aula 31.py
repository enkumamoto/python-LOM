'''
Sets em Python (conjuntos)
add(adiciona), update(atualiza), clear, discard
unio | (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esqueda)
symmetric_difference ^ (elementos que estão nos dois sets, mas não em ambos)

sets em python so suporta elementos únicos
O set usa chaves, então se não fizer da maneira correta, em vez de criar um set criará um dicionário. ou seja, não
recebe chave:valor e sim somente valor.
o set suporta elementos imutáveis e não tem índice
'''
s1 = {1,2,3,4,5,6}
print (s1)
print ('---')

# set são iteráveis
s1 = {1,2,3,4,5,6}
for v in s1:
    print (v)
print ('---')