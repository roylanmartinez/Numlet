def lrg1(x, uno=True, unn=True):
    if x == '1':
        return ' Uno' if uno else ' Un'
    elif x == '2':
        return ' Dos'
    elif x == '3':
        return ' Tres'
    elif x == '4':
        return ' Cuatro'
    elif x == '5':
        return ' Cinco'
    elif x == '6':
        return ' Seis'
    elif x == '7':
        return ' Siete'
    elif x == '8':
        return ' Ocho'
    else:
        return ' Nueve'


def lrg2(x, inti=True, uno=True, unn=True):
    if x[1] == '0':
        if x == '10':
            return ' Diez'
        elif x == '20':
            return ' Veinte'
        elif x == '30':
            return ' Treinta'
        elif x == '40':
            return ' Cuarenta'
        elif x == '50':
            return ' Cincuenta'
        elif x == '60':
            return ' Sesenta'
        elif x == '70':
            return ' Setenta'
        elif x == '80':
            return ' Ochenta'
        else:
            return ' Noventa'
    elif x[0] == '1':
        if x == '11':
            return ' Once'
        elif x == '12':
            return ' Doce'
        elif x == '13':
            return ' Trece'
        elif x == '14':
            return ' Catorce'
        elif x == '15':
            return ' Quince'
        elif x == '16':
            return ' Dieciséis'
        elif x == '17':
            return ' Diecisiete'
        elif x == '18':
            return ' Dieciocho'
        elif x == '19':
            return ' Diecinueve'
    elif x[0] == '2':
        if x == '21':
            return ' Veintiuno' if inti else ' Veintiún'
        elif x == '22':
            return ' Veintidós'
        elif x == '23':
            return ' Veintitrés'
        elif x == '24':
            return ' Veinticuatro'
        elif x == '25':
            return ' Veinticinco'
        elif x == '26':
            return ' Veinteséis'
        elif x == '27':
            return ' Veintisiete'
        elif x == '28':
            return ' Veintiocho'
        else:
            return ' Veintinueve'
    else:
        if x[0] == '3':
            return ' Treinta y' + lrg1(x[1])
        elif x[0] == '4':
            return ' Cuarenta y' + lrg1(x[1])
        elif x[0] == '5':
            return ' Cincuenta ' + lrg1(x[1])
        elif x[0] == '6':
            return ' Sesenta y' + lrg1(x[1])
        elif x[0] == '7':
            return ' Setenta y' + lrg1(x[1])
        elif x[0] == '8':
            return ' Ochenta y' + lrg1(x[1])
        else:
            return ' Noventa y' + lrg1(x[1])


def lrg3(x, inti=True, uno=True, ciento=True, unn=True):
    if x == '1':
        return ' Ciento' if ciento else ' Cien'
    elif x == '2':
        return ' Doscientos'
    elif x == '3':
        return ' Trescientos'
    elif x == '4':
        return ' Cuatrocientos'
    elif x == '5':
        return ' Quinientos'
    elif x == '6':
        return ' Seiscientos'
    elif x == '7':
        return ' Setecientos'
    elif x == '8':
        return ' Ochocientos'
    else:
        return ' Novecientos'


def lrg6(xx):
    def lrg(x, inti=True, uno=True, ciento=True, unn=True):
        if x[0] != '0':
            # verde
            if x[1] != '0':
                # verde verde
                if x[2] != '0':
                    # verde verde verde
                    return lrg3(x[0], uno, ciento) + lrg2(x[1:3], inti, uno)
                else:
                    # verde verde roja
                    return lrg3(x[0], uno, ciento) + lrg2(x[1:3])
            else:
                # verde roja
                if x[2] != '0':
                    # verde roja verde
                    return lrg3(x[0], uno, ciento) + lrg1(x[2], uno)
                else:
                    # verde roja roja
                    return lrg3(x[0], ciento)
        else:
            # roja
            if x[1] != '0':
                # roja verde
                if x[2] != '0':
                    # roja verde verde
                    return lrg2(x[1:3], inti, uno)
                else:
                    # roja verde roja
                    return lrg2(x[1:3])
            else:
                # roja roja
                if x[2] != '0':
                    # roja roja verde
                    return lrg1(x[2], uno)
                else:
                    # roja roja roja
                    return ''

    return lrg(xx[0:3], uno=False, ciento=False) + ' Mil' + lrg(xx[3:6], inti=False, ciento=False)

# for i in range(1, 1000000):
#     print(i, largo_6(str('00000' + str(i))[-6:]))
# print('Novecientos Noventa y Ocho')
# print(lrg6('101101'))
for i in range(100000, 100100):
    print(lrg6(str(i)))
# d81b3c6f5be4568572aa8db540b33dfb9f9f0e74
# asdas123123
