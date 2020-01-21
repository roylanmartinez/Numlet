class Numesp:
    def __init__(self, x):
        self.x = str(x)
        self.largo = len(self.x)
    def __str__(self):
        return self.printer()
    # UNIDADES
    def unidades(self, x, un=False,trae=''):
        if x == '0':
            return 'Cero'
        elif x == '1':
            if un == False:
                return 'Uno'
            return 'Un'
        elif x == '2':
            return 'Dos'
        elif x == '3':
            return 'Tres'
        elif x == '4':
            return 'Cuatro'
        elif x == '5':
            return 'Cinco'
        elif x == '6':
            return 'Seis'
        elif x == '7':
            return 'Siete'
        elif x == '8':
            return 'Ocho'
        else:
            return 'Nueve'

    # DECENAS
    def decenas(self, x, un=False,trae=''):
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
        else:
            return 'Noventa'
    # IMPRESOR
    def printer(self,trae=False):
        if len(self.x)==1:
            return self.unidades(self.x,False)
        elif len(self.x)==2:
            if int(self.x) in list(range(10,30))+list(range(30,101,10)):
                return self.decenas(self.x)
            else:
                return '{} y {}'.format(self.decenas(self.x[0]+'0'),self.unidades(self.x[1]))

print(Numesp(91))