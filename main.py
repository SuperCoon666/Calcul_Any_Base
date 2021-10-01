def from_10_to_any(num, base, first):
    if first != 10:
        num = int( to_10(num, base, first) )

    if base == 10:
        return num

    new = ''
    tab = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while num>0:
        new = tab[num%base] + new
        print(num, '/', base, '=', num//base, '(', num%base, ')' )
        num = num//base
    print('')
    print( '*'*(len(new)) )
    return new


def to_10(num, base, first):
    cc = list(str(num))

    tab = []
    if first>10:
        c = 10
        for i in range(len(lang)):
            tab.append([lang[i], c])
            c+=1
        for i in range(len(cc)):

            if cc[i] in lang:
                ind = lang.index(cc[i])
                cc[i] = tab[ind][1]
            else:
                cc[i] = int(cc[i])

    x = []
    res = ''
    for i in range(len(cc)-1, -1, -1):
        res+= '('+str(first)+"**"+str(i)+')'+'*'+str(cc[i])
        if i!=0:
            res+=' + '
        x.append(first**i)

    for i in range(len(x)):
        x[i] = x[i]*int(cc[i])

    print(res,'=', sum(x))
    print( '*'*(len(str(sum(x)))+3) )

    return sum(x)




def converter(base0,num, base1):
    #base0 = input('Enter your base: ')

    if base0.isdigit() and 1<int(base0)<37:
        #num = input('Enter num: ')
        base0 = int(base0)

        print(num, base0)
        if not num.isdigit() and base0<11:
            return 'err1'



        chek = list(num)
        for i in range(len(chek)):
            if chek[i].isdigit() and int(chek[i]) >= base0:
                return 'Пошёл(а) нахуй_3'

        #нужно передвинуть в другое место, чтоб при вводе буквы, не существующей в системе счисления не запрашивалась вторая система
        #base1 = input('Enter needed base: ')
        if base1.isdigit():
            base1 = int(base1)
        else:
            return'err2'

        if base0<=10:
            return from_10_to_any(int(num), base1, base0)
        else:
            num = num.upper()
            for i in range(len(num)):
                if (not num[i] in lang and not num[i].isdigit()):
                    return'Пошёл(а) нахуй_1'

                if not num[i].isdigit() and lang.index(num[i])>base0-10:
                    return 'Пошёл(а) нахуй_4'

            return from_10_to_any(num, base1, base0)
    else:
        return 'Пошёл(а) нахуй_2'


def summ(a, basea, b, baseb, answer_base):
    if basea != 10:
        a = int( converter(basea, a, '10' ))
    if baseb != 10:
        b = int( converter(baseb, b, '10' ))
    answer = a + b
    if answer_base != 10:
        answer = int( converter('10', str(answer), answer_base) )
    return answer


def rasn(a, basea, b, baseb, answer_base):
    if basea != 10:
        a = int( converter(basea, a, '10' ))
        print('gg1')
    if baseb != 10:
        b = int( converter(baseb, b, '10' ))
        print('gg2')

    answer = a - b
    if answer<0:
        answer = answer*-1

    if answer_base != 10:
        answer = int( converter('10', str(answer), answer_base) )
        print('gg3')
    return answer

def multiply(a, basea, b, baseb, answer_base):
    if basea != 10:
        a = int( converter(basea, a, '10' ))
        print('gg1')
    if baseb != 10:
        b = int( converter(baseb, b, '10' ))
        print('gg2')
    answer = a * b

    if answer_base != 10:
        answer = int( converter('10', str(answer), answer_base) )
        print('gg3')
    return answer


lang = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lang = list(lang)
#print(converter(input('Enter your base: '), input('Enter num: '), input('Enter needed base: ')  ))
#print( converter('8', '30', '2') )


#print( summ( input('Enter first num: '), input('Enter the base of this: '), input('Enter second num: '), input('Enter the base of this: '), input('Enter the base of answer: ') ) )
#print( multiply('30','8','BAB','16','2') )

command  = input("Enter number of nedeed opration ")

if command.isdigit() and int(command)==1:
    print( summ( input('Enter first num: '), input('Enter the base of this: '), input('Enter second num: '), input('Enter the base of this: '), input('Enter the base of answer: ') ) )
elif command.isdigit() and int(command)==2:
    print( rasn( input('Enter first num: '), input('Enter the base of this: '), input('Enter second num: '), input('Enter the base of this: '), input('Enter the base of answer: ') ) )
elif command.isdigit() and int(command)==3:
    print( multiply( input('Enter first num: '), input('Enter the base of this: '), input('Enter second num: '), input('Enter the base of this: '), input('Enter the base of answer: ') ) )
elif command.isdigit() and int(command)==4:
    #print( summ( input('Enter first num: '), input('Enter the base of this: '), input('Enter second num: '), input('Enter the base of this: '), input('Enter the base of answer: ') ) )
    pass
else:
    print('Incorrect, worb cant be a number')


##c = int(input())
##a = input().split()
##print(a)
##a.reverse()
##print(a)
##for i in (a):
    ##if int(i)%5==0:
        ##print(i)
        ##break
##else:
    ##print(-1)


#import random
#d5 = random.randint(1,10)
#print(d5)
