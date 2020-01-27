def largo_1(x, uno=True):
    uno = 0 if uno else -1
    unidades1 = {
        '0': [' Cero', ],
        '1': [' Uno', ' Un'],
        '2': [' Dos', ],
        '3': [' Tres', ],
        '4': [' Cuatro', ],
        '5': [' Cinco', ],
        '6': [' Seis', ],
        '7': [' Siete', ],
        '8': [' Ocho', ],
        '9': [' Nueve', ]
    }
    return unidades1[x][uno]


def largo_2(x, veintiuno=True, uno=True):
    veintiuno_1 = 0 if veintiuno else -1
    decenas1 = {
        '00': ['', ],
        '10': [' Diez', ],
        '11': [' Once', ],
        '12': [' Doce', ],
        '13': [' Trece', ],
        '14': [' Catorce', ],
        '15': [' Quince', ],
        '16': [' Dieciséis', ],
        '17': [' Diecisiete', ],
        '18': [' Dieciocho', ],
        '19': [' Diecinueve', ],
        '20': [' Veinte', ],
        '21': [' Veintiuno', ' Veintiún'],
        '22': [' Veintidós', ],
        '23': [' Veintitrés', ],
        '24': [' Veinticuatro', ],
        '25': [' Veinticinco', ],
        '26': [' Veintiséis', ],
        '27': [' Veintisiete', ],
        '28': [' Veintiocho', ],
        '29': [' Veintinueve', ],
        '30': [' Treinta', ],
        '40': [' Cuarenta', ],
        '50': [' Cincuenta', ],
        '60': [' Sesenta', ],
        '70': [' Setenta', ],
        '80': [' Ochenta', ],
        '90': [' Noventa', ]
    }
    if len(str(int(x))) == 1:
        return largo_1(x[-1], uno)
    elif int(x) in list(range(10, 30)) + list(range(30, 100, 10)):
        return decenas1[x][veintiuno_1]
    else:
        return decenas1[x[0]+'0'][veintiuno_1] + largo_1(x[1], uno)


def largo_3(x, veintiuno=True, uno=True):
    centenas1 = {
        '000': ['', ],
        '100': [' Cien', ' Ciento'],
        '200': [' Doscientos', ],
        '300': [' Trescientos', ],
        '400': [' Cuatrocientos', ],
        '500': [' Quinientos', ],
        '600': [' Seiscientos', ],
        '700': [' Setecientos', ],
        '800': [' Ochocientos', ],
        '900': [' Novecientos', ]
    }
    if len(str(int(x))) <= 2 and x != '000':
        return largo_2(x[1:3], uno)
    else:
        if x == '000':
            return centenas1[x][0]
        elif int(x) in range(100, 901, 100):
            return centenas1[x][0]
        else:
            return centenas1[x[0] + '00'][-1] + largo_2(x[1:3], veintiuno, uno)


def largo_6(x):
    y = ' Mil'
    if len(str(int(x[0:3]))) == 1 and x[0:3] != '000':
        if x[2] == '1':
            return y + largo_3(x[3:6])
        else:
            return largo_1(x[2]) + y + largo_3(x[3:6])
    elif len(str(int(x[0:3]))) == 2:
        return largo_2(x[1:3], veintiuno=False, uno=False) + y + largo_3(x[3:6])
    elif len(str(int(x[0:3]))) == 3:
        return largo_3(x[0:3], veintiuno=False, uno=False) + y + largo_3(x[3:6])
    else:
        return largo_3(x[3:6])
for i in range(100000, 1000000):
    largo_6(str(i))

# for i in range(1, 1000000):
#     print(i, largo_6(str('00000' + str(i))[-6:]))
# print('Novecientos Noventa y Ocho')
# print(largo_6('000001'))
# for i in range(1, 1000000):
#     largo_6(str('00000' + str(i))[-6:])
#d81b3c6f5be4568572aa8db540b33dfb9f9f0e74
#test