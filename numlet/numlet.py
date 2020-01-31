# IZQUIERDA DEL MIL
def n(x):
    if x == '1':
        return ' Un'
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


def nn(x):
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
            return ' Veintiún'
        elif x == '21':
            return ' Veintiuno'
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
        return ''.join([' Treinta', '' if x[1] == 0 else ' y{}'.format(n(x[1]))])
    elif x[0] == '4':
        return ''.join([' Cuarenta', '' if x[1] == 0 else ' y{}'.format(n(x[1]))])
    elif x[0] == '5':
        return ''.join([' Cincuenta', '' if x[1] == 0 else ' y{}'.format(n(x[1]))])
    elif x[0] == '6':
        return ''.join([' Sesenta', '' if x[1] == 0 else ' y{}'.format(n(x[1]))])
    elif x[0] == '7':
        return ''.join([' Setenta', '' if x[1] == 0 else ' y{}'.format(n(x[1]))])
    elif x[0] == '8':
        return ''.join([' Ochenta', '' if x[1] == 0 else ' y{}'.format(n(x[1]))])
    elif x[0] == '9':
        return ''.join([' Noventa', '' if x[1] == 0 else ' y{}'.format(n(x[1]))])
    else:
        if int(x) == 0:
            ''
        return n(x[1])


def nnn(x):
    if x[0] == '1':
        if x[1:3] == '00':
            return ' Cien'
        else:
            return ''.join([' Ciento', nn(x[1:3])])
    elif x[0] == '2':
        return ''.join([' Doscientos', '' if x[0] == '0' else nn(x[1:3])])
    elif x[0] == '3':
        return ''.join([' Trescientos', '' if x[0] == '0' else nn(x[1:3])])
    elif x[0] == '4':
        return ''.join([' Cuatrocientos', '' if x[0] == '0' else nn(x[1:3])])
    elif x[0] == '5':
        return ''.join([' Quinientos', '' if x[0] == '0' else nn(x[1:3])])
    elif x[0] == '6':
        return ''.join([' Seiscientos', '' if x[0] == '0' else nn(x[1:3])])
    elif x[0] == '7':
        return ''.join([' Setecientos', '' if x[0] == '0' else nn(x[1:3])])
    elif x[0] == '8':
        return ''.join([' Ochocientos', '' if x[0] == '0' else nn(x[1:3])])
    elif x[0] == '9':
        return ''.join([' Novecientos', '' if x[0] == '0' else nn(x[1:3])])
    else:
        # 0 N N
        return nn(x[1:3])


# DERECHA DEL MIL
def ni(x):
    if x == '1':
        return ' Mil Uno'
    elif x == '2':
        return ' Mil Dos'
    elif x == '3':
        return ' Mil Tres'
    elif x == '4':
        return ' Mil Cuatro'
    elif x == '5':
        return ' Mil Cinco'
    elif x == '6':
        return ' Mil Seis'
    elif x == '7':
        return ' Mil Siete'
    elif x == '8':
        return ' Mil Ocho'
    else:
        return ' Mil Nueve'


def nni(x):
    if x[0] == '1':
        if x == '10':
            return ' Mil Diez'
        elif x == '11':
            return ' Mil Once'
        elif x == '12':
            return ' Mil Doce'
        elif x == '13':
            return ' Mil Trece'
        elif x == '14':
            return ' Mil Catorce'
        elif x == '15':
            return ' Mil Quince'
        elif x == '16':
            return ' Mil Dieciséis'
        elif x == '17':
            return ' Mil Diecisiete'
        elif x == '18':
            return ' Mil Dieciocho'
        else:
            # 19
            return ' Mil Diecinueve'
    elif x[0] == '2':
        # dos
        if x == '20':
            return ' Mil Veinte'
        elif x == '21':
            return ' Mil Veintiuno'
        elif x == '22':
            return ' Mil Veintidós'
        elif x == '23':
            return ' Mil Veintitrés'
        elif x == '24':
            return ' Mil Veinticuatro'
        elif x == '25':
            return ' Mil Veinticinco'
        elif x == '26':
            return ' Mil Veinteséis'
        elif x == '27':
            return ' Mil Veintisiete'
        elif x == '28':
            return ' Mil Veintiocho'
        else:
            # 29
            return ' Mil Veintinueve'
    elif x[0] == '3':
        return ''.join([' Mil Treinta', '' if x[1] == 0 else ' y{}'.format(ni(x[1]))])
    elif x[0] == '4':
        return ''.join([' Mil Cuarenta', '' if x[1] == 0 else ' y{}'.format(ni(x[1]))])
    elif x[0] == '5':
        return ''.join([' Mil Cincuenta', '' if x[1] == 0 else ' y{}'.format(ni(x[1]))])
    elif x[0] == '6':
        return ''.join([' Mil Sesenta', '' if x[1] == 0 else ' y{}'.format(ni(x[1]))])
    elif x[0] == '7':
        return ''.join([' Mil Setenta', '' if x[1] == 0 else ' y{}'.format(ni(x[1]))])
    elif x[0] == '8':
        return ''.join([' Mil Ochenta', '' if x[1] == 0 else ' y{}'.format(ni(x[1]))])
    elif x[0] == '9':
        return ''.join([' Mil Noventa', '' if x[1] == 0 else ' y{}'.format(ni(x[1]))])
    else:
        if int(x) == 0:
            ''
        return ni(x[1])


def nnni(x):
    if x[0] == '1':
        if x[1:3] == '00':
            return ' Mil Cien'
        else:
            return ''.join([' Mil Ciento', nni(x[1:3])])
    elif x[0] == '2':
        return ''.join([' Mil Doscientos', '' if x[0] == '0' else nni(x[1:3])])
    elif x[0] == '3':
        return ''.join([' Mil Trescientos', '' if x[0] == '0' else nni(x[1:3])])
    elif x[0] == '4':
        return ''.join([' Mil Cuatrocientos', '' if x[0] == '0' else nni(x[1:3])])
    elif x[0] == '5':
        return ''.join([' Mil Quinientos', '' if x[0] == '0' else nni(x[1:3])])
    elif x[0] == '6':
        return ''.join([' Mil Seiscientos', '' if x[0] == '0' else nni(x[1:3])])
    elif x[0] == '7':
        return ''.join([' Mil Setecientos', '' if x[0] == '0' else nni(x[1:3])])
    elif x[0] == '8':
        return ''.join([' Mil Ochocientos', '' if x[0] == '0' else nni(x[1:3])])
    elif x[0] == '9':
        return ''.join([' Mil Novecientos', '' if x[0] == '0' else nni(x[1:3])])
    else:
        # 0 N N
        return nni(x[1:3])


# COMPACTADOR DE MIL

def nnn6(x):
    return ''.join([nnn(x[0:3]), nnni(x[3:6])])

print(nnn6('123123'))
# asd123123