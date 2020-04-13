#Gerador de jogos na Mega -

import random as r

# a=b a=c a=d a=e a=f b=c b=d b=e b=f c=d c=e c=f d=e d=f e=f    :::: possibilidades

qtd = int(input("Quantos jogos você quer fazer ?\n"))
feitos = 0
while feitos < qtd :
    a,b,c,d,e,f = r.randint(1, 60),r.randint(1, 60),r.randint(1, 60),r.randint(1, 60),r.randint(1, 60),r.randint(1, 60)
    while a == b or a==c or a==d or a==e or a==f or b==c or b==d or b==e or b==f or c==d or c==e or c==f or d==e or d==f or e==f: #nao repetir na mesma linha
        a,b,c,d,e,f = r.randint(1, 60),r.randint(1, 60),r.randint(1, 60),r.randint(1, 60),r.randint(1, 60),r.randint(1, 60)
    print(a, b, c, d, e, f)
    feitos += 1
