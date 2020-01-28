def largo_1(x, uno=True, unn=True):
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


def largo_2(x, veintiuno=True, uno=True, unn=True):
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
            return ' Veintiuno' if veintiuno else ' Veintiún'
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
            return ' Treinta y' + largo_1(x[1], uno)
        elif x[0] == '4':
            return ' Cuarenta y' + largo_1(x[1], uno)
        elif x[0] == '5':
            return ' Cincuenta y' + largo_1(x[1], uno)
        elif x[0] == '6':
            return ' Sesenta y' + largo_1(x[1], uno)
        elif x[0] == '7':
            return ' Setenta y' + largo_1(x[1], uno)
        elif x[0] == '8':
            return ' Ochenta y' + largo_1(x[1], uno)
        else:
            return ' Noventa y' + largo_1(x[1], uno)


def largo_3(x, veintiuno=True, uno=True, unn=True):
    if x[0] == '0':
        if x == '000':
            return ''
        elif x[1:3] == '00':
            # 0 0 N
            return largo_1(x[1:3], uno, unn)
        else:
            # 0 N N
            return largo_2(x[1:3], veintiuno, uno, unn)
    else:
        if x[1] == '0':
            if x[1:3] == '00':
                # N 0 0
                if x == '100':
                    return ' Cien'
                elif x == '200':
                    return ' Doscientos'
                elif x == '300':
                    return ' Trescientos'
                elif x == '400':
                    return ' Cuatrocientos'
                elif x == '500':
                    return ' Quinientos'
                elif x == '600':
                    return ' Seiscientos'
                elif x == '700':
                    return ' Setecientos'
                elif x == '800':
                    return ' Ochocientos'
                else:
                    return ' Novecientos'
            else:
                # N 0 N
                if x[0] == '1':
                    return ' Ciento' + largo_1(x[2], uno, unn)
                elif x[0] == '0':
                    return ' Doscientos' + largo_1(x[2], uno, unn)
                elif x[0] == '3':
                    return ' Trescientos' + largo_1(x[2], uno, unn)
                elif x[0] == '4':
                    return ' Cuatrocientos' + largo_1(x[2], uno, unn)
                elif x[0] == '5':
                    return ' Quinientos' + largo_1(x[2], uno, unn)
                elif x[0] == '6':
                    return ' Seiscientos' + largo_1(x[2], uno, unn)
                elif x[0] == '7':
                    return ' Setecientos' + largo_1(x[2], uno, unn)
                elif x[0] == '8':
                    return ' Ochocientos' + largo_1(x[2], uno, unn)
                else:
                    return ' Novecientos' + largo_1(x[2], uno, unn)
        else:
            # N N N
            if x[0] == '1':
                return ' Ciento' + largo_2(x[1:3], veintiuno, uno, unn)
            elif x[0] == '2':
                return ' Doscientos' + largo_2(x[1:3], veintiuno, uno, unn)
            elif x[0] == '3':
                return ' Trescientos' + largo_2(x[1:3], veintiuno, uno, unn)
            elif x[0] == '4':
                return ' Cuatrocientos' + largo_2(x[1:3], veintiuno, uno, unn)
            elif x[0] == '5':
                return ' Quinientos' + largo_2(x[1:3], veintiuno, uno, unn)
            elif x[0] == '6':
                return ' Seiscientos' + largo_2(x[1:3], veintiuno, uno, unn)
            elif x[0] == '7':
                return ' Setecientos' + largo_2(x[1:3], veintiuno, uno, unn)
            elif x[0] == '8':
                return ' Ochocientos' + largo_2(x[1:3], veintiuno, uno, unn)
            else:
                return ' Novecientos' + largo_2(x[1:3], veintiuno, uno, unn)


def largo_6(x, unn=True):
    y = ' Mil'
    if x[0:3] != '000':
        return largo_3(x[3:6])
    elif len(str(int(x[0:3]))) == 1:
        if x[2] == '1':
            return y + largo_3(x[3:6])
        else:
            return largo_1(x[2]) + y + largo_3(x[3:6])
    elif len(str(int(x[0:3]))) == 2:
        return largo_2(x[1:3], veintiuno=False, uno=False) + y + largo_3(x[3:6])
    else:
        return largo_3(x[0:3], veintiuno=False, uno=False) + y + largo_3(x[3:6])

    # elif x[0:2] == '00':
    #     if x[2] == '1':
    #         return ' Mil' + largo_3(x[3:6], unn)
    #     else:
    #         return largo_1(x[2]) + ' Mil' + largo_3(x[3:6], unn)
    # elif x[0] == '0':
    #     return largo_2(x[1:3], veintiuno=False, uno=False) + ' Mil' + largo_3(x[3:6], unn)
    # else:
    #     return largo_3(x[0:3], veintiuno=False, uno=False) + ' Mil' + largo_3(x[3:6], unn)


# for i in range(1000, 1231):
#     largo_6(str(i))

# for i in range(1, 1000000):
#     print(i, largo_6(str('00000' + str(i))[-6:]))
# print('Novecientos Noventa y Ocho')
print(largo_6('101101'))
# for i in range(1, 1000000):
#     largo_6(str('00000' + str(i))[-6:])
#d81b3c6f5be4568572aa8db540b33dfb9f9f0e74
#asdas123123