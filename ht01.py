from random import randint

print('Игровое поле:')
array = [['1','2','3'],['4','5','6'],['7','8','9']]

def printArr(array):
    for row in array:
        print (row)
printArr(array)

def userEnt():
    num1 = input('Укажите номер ячейки, в которую поставить X: ')
    for i in range(0,3):
        for j in range(0,3):
            if num1 == array[i][j]:
                array[i][j] = "x"

            
def iiEnt():
    print('Ход компьютера')
    comp = False
    while comp == False:
        i = randint(0,2)
        j = randint(0,2)
        if array[i][j] != "x" and  array[i][j] != 'o':
            array[i][j]  = 'o'
            comp = True 
        else: comp = False                

def cheсk1(array):
    for i in range(0,3):
        if (array[i][0] == 'x' and array[i][1] == 'x' and array[i][2] == 'x'):
            print("Победил игрок")
            return True
        if (array[i][0] == 'o' and array[i][1] == 'o' and array[i][2] == 'o'):
            print("Победил компьютер")
            return True
    else:
        return False

def cheсk2(array):
    for j in range(0,3):
        if (array[0][j] == 'x' and array[1][j] == 'x' and array[2][j] == 'x'):
            print("Победил игрок")
            return True
        if (array[0][j] == 'o' and array[1][j] == 'o' and array[2][j] == 'o'):
            print("Победил компьютер")
            return True
    else:
        return False

def check3diagonal(array):
    if (array[0][0] == 'x' and array[1][1] == 'x' and array[2][2] == 'x') or (
        array[0][2] == 'x'and array[1][1] == 'x' and array[2][0] == 'x'
    ):
        print('Победил игрок')
        return True
    if (array[0][0] == 'o' and array[1][1] == 'o' and array[2][2] == 'o') or (
        array[0][2] == 'o' and array[1][1] == 'o'and array[2][0] == 'o'
    ):
        print('Победил компьютер')
        return True
    else:
        return False
    

end = False
while end == False:
    userEnt()
    printArr(array)
    iiEnt()
    printArr(array)
    if cheсk1(array) == True or cheсk2(array) == True or check3diagonal(array) == True:
        end = True
    
        
           
