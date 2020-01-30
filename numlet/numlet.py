def unidades(x, un=False, uno=True):
    if x == '0' or x == '00' or x == '000':
        return 'Cero'
    elif x == '1' or x == '01' or x == '001':
        if uno:
            return 'Uno'
        else:
            return 'Un'
    elif x == '2' or x == '02' or x == '002':
        return 'Dos'
    elif x == '3' or x == '03' or x == '003':
        return 'Tres'
    elif x == '4' or x == '04' or x == '004':
        return 'Cuatro'
    elif x == '5' or x == '05' or x == '005':
        return 'Cinco'
    elif x == '6' or x == '06' or x == '006':
        return 'Seis'
    elif x == '7' or x == '07' or x == '007':
        return 'Siete'
    elif x == '8' or x == '08' or x == '008':
        return 'Ocho'
    elif x == '9' or x == '09' or x == '009':
        return 'Nueve'
    else:
        return 'error'


def decenas(x, un=False):
    if x == '10' or x == '010':
        return 'Diez'
    elif x == '11' or x == '011':
        return 'Once'
    elif x == '12' or x == '012':
        return 'Doce'
    elif x == '13' or x == '013':
        return 'Trece'
    elif x == '14' or x == '014':
        return 'Catorce'
    elif x == '15' or x == '015':
        return 'Quince'
    elif x == '16' or x == '016':
        return 'Dieciséis'
    elif x == '17' or x == '017':
        return 'Diecisiete'
    elif x == '18' or x == '018':
        return 'Dieciocho'
    elif x == '19' or x == '019':
        return 'Diecinueve'
    elif x == '20' or x == '020':
        return 'Veinte'
    elif x == '21' or x == '021':
        if un:
            return 'Veintiún'
        else:
            return 'Veintiuno'
    elif x == '22' or x == '022':
        return 'Veintidós'
    elif x == '23' or x == '023':
        return 'Veintitrés'
    elif x == '24' or x == '024':
        return 'Veinticuatro'
    elif x == '25' or x == '025':
        return 'Veinticinco'
    elif x == '26' or x == '026':
        return 'Veinteséis'
    elif x == '27' or x == '027':
        return 'Veintisiete'
    elif x == '28' or x == '028':
        return 'Veintiocho'
    elif x == '29' or x == '029':
        return 'Veintinueve'
    elif x == '30' or x == '030':
        return 'Treinta'
    elif x == '40' or x == '040':
        return 'Cuarenta'
    elif x == '50' or x == '050':
        return 'Cincuenta'
    elif x == '60' or x == '060':
        return 'Sesenta'
    elif x == '70' or x == '070':
        return 'Setenta'
    elif x == '80' or x == '080':
        return 'Ochenta'
    elif x == '90' or x == '090':
        return 'Noventa'
    else:
        return unidades(x)


def centenas(x, ciento=False):
    if x == '100':
        if ciento:
            return 'Ciento'
        else:
            return 'Cien'
    elif x == '200':
        return 'Doscientos'
    elif x == '300':
        return 'Trescientos'
    elif x == '400':
        return 'Cuatrocientos'
    elif x == '500':
        return 'Quinientos'
    elif x == '600':
        return 'Seiscientos'
    elif x == '700':
        return 'Setecientos'
    if x == '800':
        return 'Ochocientos'
    if x == '900':
        return 'Novecientos'
    else:
        return decenas(x[1:])


def base(x, un=False, uno=True):
    if len(x) == 1:
        return unidades(x)
    elif len(x) == 2:
        if x[-1] == '0':
            return decenas(x)
        elif x[0] == '0':
            return unidades(x[0])
        elif int(x) in list(range(10, 30))+list(range(30, 100, 10)):
            if un:
                return decenas(x, un=True)
            else:
                return decenas(x)
        else:
            return '{} y {}'.format(decenas(x[0] + '0'), unidades(x[-1]))
    elif len(x) == 3:
        if x[0:2] == '00':
            return unidades(x)
        if x[0] == '0':
            if int(x[1:]) in list(range(10, 30))+list(range(30, 100, 10)):
                if un:
                    return decenas(x, un=True)
                else:
                    return decenas(x)
            else:
                if un:
                    return '{} y {}'.format(decenas(x[1] + '0', un=True), unidades(x[-1]))
                else:
                    return '{} y {}'.format(decenas(x[1] + '0'), unidades(x[-1]))
        if x[1:] == '00':
            return centenas(x)
        elif x[0] != 0 and x[1] == '0' and x[-1] != '0':
            if uno:
                return '{} {}'.format(centenas(x[0] + '00', ciento=True),
                                      unidades(x[-1]))
            else:
                return '{} {}'.format(centenas(x[0] + '00', ciento=True),
                                      unidades(x[-1], uno=False))
        elif int(x[1:]) in list(range(10, 30))+list(range(30, 100, 10)):
            if un:
                return '{} {}'.format(centenas(x[0] + '00', ciento=True),
                                      decenas(x[1:], un=True))
            else:
                return '{} {}'.format(centenas(x[0] + '00', ciento=True),
                                      decenas(x[1:]))
        else:
            return '{} {} y {}'.format(centenas(x[0] + '00', ciento=True),
                                       decenas(x[1]+'0'),
                                       unidades(x[-1]))
    else:
        return 'error'


def mil(x):
    y = 'Mil'
    if len(str(int(x))) == 4:
        if x[3:6] == '000':
            if x[2] == '1':
                return y
            else:
                return f'{base(x[2])} {y}'
        else:
            if x[2] == '1':
                return f'{y} {base(x[3:6])}'
            else:
                return '{} {} {}'.format(base(x[2]), y, base(x[3:6]))
    elif len(str(int(x))) == 5:
        if x[3:6] == '000':
            return f'{base(x[:3])} {y}'
        else:
            return '{} {} {}'.format(base(x[1:3]), y, base(x[3:6]))
    else:
        if x[1:3] == '01':
            if x[3:6] == '000':
                return f'{base(x[:3], uno=False)} {y}'
            else:
                return '{} {} {}'.format(base(x[:3], uno=False), y, base(x[3:6]))
        else:
            if x[3:6] == '000':
                return '{} {}'.format(base(x[:3], un=True), y)
            else:
                return '{} {} {}'.format(base(x[:3], un=True), y, base(x[3:6], un=True))

print(mil('001000'))

# class Numlet:
#
#     def __init__(self, x):
#         self.x = str(x)
#         self.largo = len(str(x))
#         self.resto = x % 6
#
#     def __str__(self):
#         if self.largo < 4:
#             return base(self.x)
#         elif self.largo < 7:
#             return mil((5*'0'+self.x)[-6:])