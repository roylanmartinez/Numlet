class Numesp:
    def __init__(self, x):
        self.x = str(x)
        self.largo = len(self.x)

    def __str__(self):
        if 1 <= self.largo <= 3:
            doo = 'self.tres(self.x)'
        if 4 <= self.largo <= 6:
            doo = 'self.seis(self.x)'
        return eval(doo)

    # UNIDADES
    def unidades(self, x, un=False, trae=''):
        if x == '1' or x == '01' or x == '001':
            if un == False:
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

    # DECENAS
    def decenas(self, x, un=False, trae=''):
        if x == '10':
            return 'Diez'
        elif x == '11':
            return 'Once'
        elif x == '12':
            return 'Doce'
        elif x == '13':
            return 'Trece'
        elif x == '14':
            return 'Catorce'
        elif x == '15':
            return 'Quince'
        elif x == '16':
            return 'Dieciséis'
        elif x == '17':
            return 'Diecisiete'
        elif x == '18':
            return 'Dieciocho'
        elif x == '19':
            return 'Diecinueve'
        elif x == '20':
            return 'Veinte'
        elif x == '21':
            if un == True:
                return 'veintiún'
            return 'Veintiuno'
        elif x == '22':
            return 'Veintidós'
        elif x == '23':
            return 'Veintitrés'
        elif x == '24':
            return 'Veinticuatro'
        elif x == '25':
            return 'Veinticinco'
        elif x == '26':
            return 'Veinteséis'
        elif x == '27':
            return 'Veintisiete'
        elif x == '28':
            return 'Veintinueve'
        elif x == '30':
            return 'Treinta'
        elif x == '40':
            return 'Cuarenta'
        elif x == '50':
            return 'Cincuenta'
        elif x == '60':
            return 'Sesenta'
        elif x == '70':
            return 'Setenta'
        elif x == '80':
            return 'Ochenta'
        elif x == '90':
            return 'Noventa'
        else:
            return self.unidades(x)

    def centenas(self, x, ciento=False):
        if x == '100':
            if ciento == True:
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
            return self.decenas(x)

    def tres(self, x, trae=False):
        if len(str(x)) == 1:
            return self.unidades(x, False)
        elif len(x) == 2:
            if int(x) in list(range(10, 30)) + list(range(30, 101, 10)):
                return self.decenas(x)
            else:
                return '{} y {}'.format(self.decenas(x[0] + '0'), self.unidades(x[1]))
        elif len(str(x)) == 3:
            if int(x) in list(range(100, 1001, 100)):
                return self.centenas(x)
            else:
                return '{} {} y {}'.format(self.centenas(x[0] + '00', ciento=True), self.decenas(x[1] + '0'),
                                           self.unidades(x[2]))
        else:
            return 'error'

    def seis(self, x, trae=False):
        if x[-3:]=='000':
            if x[0]=='1':
                return 'Mil'
            else:
                return self.tres(x[0])+' Mil'
        elif (1000 <= int(x) < 2000):
            return 'Mil ' + self.tres(x[1:])
        elif (3 < len(x) <= 6):
            return '{} Mil {}'.format(x[0:len(x) - 3],self.tres(x[-3:]))
        else:
            return 'error'


print('', Numesp(1001))
