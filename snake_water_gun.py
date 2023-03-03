import random
def gameWin(comp, you):
    if comp == you:
        return
    elif comp=="s":
        if you=='w':
            return False
        elif you=='g':
            return True
    
    elif comp=='w':
        if you=='s':
            return True
        elif you == 'g':
            return False
    
    elif comp=='g':
        if you=='s':
            return False
        elif you=="w":
            return True
comp = print('comp turn : Snake(s) Water (w) or gun(g)?')
randNO =random.randint(1,3)
print(randNO)
if randNO==1:
    comp =='s'
elif randNO==2:
    comp =='w'
elif randNO==3:
    comp =='g'
you = input('your turn : snake(s) or water(w) or gun(g)')

a =gameWin(comp,you)

print(f'comp chose{comp}')
print(f'you chose{you}')

if (a==None):
    print('tie!')
elif (a==True):
    print('cograts, you won!')
else:
    print('Sorry!, you loose.')