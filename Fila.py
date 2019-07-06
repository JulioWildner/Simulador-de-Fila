play = True
idoso=[]
gestante=[]
normal=[]
print('=----------------------------------------------------------------------=-')
print('= INTERAÇÃO COM A FILA:    -  IIIIIII  IIIIIIII  II            II        =- ')
print('=                          -  II          II     II           IIII        =-')
print('=> Adicionar alguém -> (1) -  IIIIII      II     II          II  II        =-')
print('=> Avançar fila -----> (2) -  II          II     II         II    II       =-')
print('=> Ver a fila -------> (3) -  II          II     II        IIIIIIIIII     =-')  
print('=> Sair -------------> (9) -  II       IIIIIIII  IIIIIII  II        II   =-')
print('=-----------------------------------------------------------------------=-')
ido = 1; ges = 1; nor = 1;
while play:
    x = int(input('=> O que gostaria de fazer: '))
    if x == 1:
        print('=----------------------=-')
        print('Add Idoso ----> ( 1 )')
        print('Add Gestante -> ( 2 )')
        print('Add Normal ---> ( 3 )')
        print('=----------------------=-')
        y = int(input('Quem?: '))
        if y == 1:
            idoso.append('A'+str(ido))
            print('=----------------------=-')
            print('Idoso entrou com senha A%s'%ido)
            ido+=1
        elif y == 2:
            gestante.append('B'+str(ges))
            print('=----------------------=-')
            print('Gestante entrou com senha B%s'%ges)
            ges+=1
        elif y == 3:
            normal.append('C'+str(nor))
            print('=----------------------=-')
            print('Normal entrou com senha C%s'%nor)
            nor+=1
        else:
            print('INVÁLIDO!!!')
    elif x == 2:
        if len(idoso) > 0:
            print('Idoso com senha %s saiu'%idoso[0])
            idoso.remove(idoso[0])
        elif len(gestante) > 0:
            print('Gestante com senha %s saiu'%gestante[0])
            gestante.remove(gestante[0])
        elif len(normal) > 0:
            print('Normal com senha %s saiu'%normal[0])
            normal.remove(normal[0])
        else:
            print('Fila vazia!')
    elif x == 3:
        print('Fila dos Idosos ---->',', '.join(idoso))
        print('Fila das Gestantes ->',', '.join(gestante))
        print('Fila de Normais ---->',', '.join(normal))
    elif x == 9:
        play = False
    else:
        print('INVÁLIDO!!!')
