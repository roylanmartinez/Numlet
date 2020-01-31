def ni(x, bef=True):
    if x == '1':
        return ' Uno' if bef else ' Un'
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
    elif x == '9':
        return ' Nueve'
    else:
        return ''


def nni(x, bef=True):
    if x[0] == '1':
        if x == '10':
            return ' Diez'
        elif x == '11':
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
        else:
            # 19
            return ' Diecinueve'
    elif x[0] == '2':
        # dos
        if x == '20':
            return ' Veinte'
        elif x == '21':
            return ' Veintiuno' if bef else ' Veintiún'
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
            # 29
            return ' Veintinueve'
    elif x[0] == '3':
        return ''.join([' Treinta', '' if x[1] == 0 else ' y{}'.format(ni(x[1], bef))])
    elif x[0] == '4':
        return ''.join([' Cuarenta', '' if x[1] == 0 else ' y{}'.format(ni(x[1], bef))])
    elif x[0] == '5':
        return ''.join([' Cincuenta', '' if x[1] == 0 else ' y{}'.format(ni(x[1], bef))])
    elif x[0] == '6':
        return ''.join([' Sesenta', '' if x[1] == 0 else ' y{}'.format(ni(x[1], bef))])
    elif x[0] == '7':
        return ''.join([' Setenta', '' if x[1] == 0 else ' y{}'.format(ni(x[1], bef))])
    elif x[0] == '8':
        return ''.join([' Ochenta', '' if x[1] == 0 else ' y{}'.format(ni(x[1], bef))])
    elif x[0] == '9':
        return ''.join([' Noventa', '' if x[1] == 0 else ' y{}'.format(ni(x[1], bef))])
    else:
        return ni(x[1], bef)


def nnni(x, bef=True):
    if x[0] == '1':
        if x[1:3] == '00':
            return ' Cien'
        else:
            return ''.join([' Ciento', nni(x[1:3], bef)])
    elif x[0] == '2':
        return ''.join([' Doscientos', '' if x[1:3] == '00' else nni(x[1:3], bef)])
    elif x[0] == '3':
        return ''.join([' Trescientos', '' if x[1:3] == '00' else nni(x[1:3], bef)])
    elif x[0] == '4':
        return ''.join([' Cuatrocientos', '' if x[1:3] == '00' else nni(x[1:3], bef)])
    elif x[0] == '5':
        return ''.join([' Quinientos', '' if x[1:3] == '00' else nni(x[1:3], bef)])
    elif x[0] == '6':
        return ''.join([' Seiscientos', '' if x[1:3] == '00' else nni(x[1:3], bef)])
    elif x[0] == '7':
        return ''.join([' Setecientos', '' if x[1:3] == '00' else nni(x[1:3], bef)])
    elif x[0] == '8':
        return ''.join([' Ochocientos', '' if x[1:3] == '00' else nni(x[1:3], bef)])
    elif x[0] == '9':
        return ''.join([' Novecientos', '' if x[1:3] == '00' else nni(x[1:3], bef)])
    else:
        # 0 N N
        return nni(x[1:3], bef)


def nnn6(x, bef=True):
    if x == '000000':
        return ''
    elif x[0:3] == '001':
        return ''.join([' Mil', nnni(x[3:6], bef)])
    elif x[0:3] == '000':
        return nnni(x[3:6], bef)
    else:
        return ''.join([nnni(x[0:3], bef=False), ' Mil', nnni(x[3:6], bef)])


print(nnn6('122201', bef=False))

# COMPACTADOR DE MIL

# def nnn6(x):
#     return ''.join([nnni(x[0:3]), nnni(x[3:6])])
