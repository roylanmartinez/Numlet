"""
   La librería de numlet.py te permite convertir más de 10^600 números naturales distintos, incluido el cero, a letras.
   La clase 'Numeros' toma como parámetro un integer y mediante el método 'a_letras' retorna un string.
   Por lo tanto, a la hora de retornar un resultado se le pueden asociar métodos subordinados a objetos de carácter str,
   por ejemplo .lower() y además también se puede ingresar un input asociado a métodos de carácter int, por ejemplo,
   abs(*cantidad negativa).

   Las instrucciones están dentro de la clase Numero.

   ¡Espero que les guste!

   Repositorio: https://github.com/roylanmartinez/Numlet
"""


# Bases para intermedios: ni(), nni() y nnni()
def ni(x: str, bef=True):
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
        # elif x == '0':
        return ''


def nni(x: str, bef=True):
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
            # elif x == '18':
            return ' Diecinueve'
    elif x[0] == '2':
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
            # elif x == '29':
            return ' Veintinueve'
    elif x[0] == '3':
        return ''.join([' Treinta', '' if x[1] == '0' else ''.join([' y', ni(x[1], bef)])])
    elif x[0] == '4':
        return ''.join([' Cuarenta', '' if x[1] == '0' else ''.join([' y', ni(x[1], bef)])])
    elif x[0] == '5':
        return ''.join([' Cincuenta', '' if x[1] == '0' else ''.join([' y', ni(x[1], bef)])])
    elif x[0] == '6':
        return ''.join([' Sesenta', '' if x[1] == '0' else ''.join([' y', ni(x[1], bef)])])
    elif x[0] == '7':
        return ''.join([' Setenta', '' if x[1] == '0' else ''.join([' y', ni(x[1], bef)])])
    elif x[0] == '8':
        return ''.join([' Ochenta', '' if x[1] == '0' else ''.join([' y', ni(x[1], bef)])])
    elif x[0] == '9':
        return ''.join([' Noventa', '' if x[1] == '0' else ''.join([' y', ni(x[1], bef)])])
    else:
        #  elif x[0] == '0':
        return ni(x[1], bef)


def nnni(x: str, bef=True):
    if x[0] == '1':
        if x[1:] == '00':
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
        # elif x[0] == '0':
        return nni(x[1:], bef)


# Compactador de menores de un millon: n6()
def n6(x: str, bef=True):
    if x == '000000':
        return ''
    elif x[:3] == '001':
        return ''.join([' Mil', nnni(x[3:], bef)])
    elif x[:3] == '000':
        return nnni(x[3:], bef)
    else:
        return ''.join([nnni(x[:3], bef=False), ' Mil', nnni(x[3:], bef)])


# Compactador de intermedios y tipo de cantidad en singular y plural (v1 y v2): ninf()
def ninf(x: str, v1=' Un Millón', v2=' Millones'):
    if x == '000000':
        return ''
    elif x == '000001':
        return v1
    else:
        return ''.join([n6(x, bef=False), v2])


# Administrador en forma de clase:
class Numero:
    """
    Esta clase básicamente controla el uso de las funciones compactadores ninf() y n6(), que a su vez coordinan el uso
    de las funciones base ni(), nni() y nnni(). Además, incluye los datos que posteriormente se ordenan y se pasan
    como parámetros al método a_letras() mediante el atributo a_letras.

       Forma de uso:

    Primer ejemplo:
       n = 1210
       resultado = Numero(n).a_letras
       print(resultado)
       --- Mil Doscientos Diez

    Segundo ejemplo:
        n = 1210
        resultado = Numero(n).a_letras.lower()
        print(resultado)
       --- mil doscientos diez

    Tercer ejemplo:
        n = abs(-121*10)
        resultado = Numero(n).a_letras.upper()
        print(resultado)
       --- MIL DOSCIENTOS DIEZ

    """
    base = [
        [' Un Centillón', ' Centillones'],
        [' Un Novenonigintillón', ' Novenonigintillones'], [' Un Octononigintillón', ' Octononigintillones'],
        [' Un Septenonigintillón', ' Septenonigintillones'], [' Un Sexvigintillón', ' Sexvigintillones'],
        [' Un Quinonintillón', ' Quinonigintillones'], [' Un Cuatornonigintillón', ' Cuatornonigintillones'],
        [' Un Trenonigintillón', ' Trenonigintillones'], [' Un Duononigintillón', ' Duononigintillones'],
        [' Un Unonigintillón', ' Unonigintillones'], [' Un Nonigintillón', ' Nonigintillones'],
        [' Un Novenoctigintillón', ' Novenoctigintillones'], [' Un Octooctigintillón', ' Octooctigintillones'],
        [' Un Septenoctigintillón', ' Septenoctigintillones'], [' Un Sexvigintillón', ' Sexvigintillones'],
        [' Un Quinoctintillón', ' Quinoctigintillones'], [' Un Cuatoroctigintillón', ' Cuatoroctigintillones'],
        [' Un Treoctigintillón', ' Treoctigintillones'], [' Un Duooctigintillón', ' Duooctigintillones'],
        [' Un Unoctigintillón', ' Unoctigintillones'], [' Un Octigintillón', ' Octigintillones'],
        [' Un Novenseptigintillón', ' Novenseptigintillones'], [' Un Octoseptigintillón', ' Octoseptigintillones'],
        [' Un Septenseptigintillón', ' Septenseptigintillones'], [' Un Sexvigintillón', ' Sexvigintillones'],
        [' Un Quinseptintillón', ' Quinseptigintillones'], [' Un Cuatorseptigintillón', ' Cuatorseptigintillones'],
        [' Un Treseptigintillón', ' Treseptigintillones'], [' Un Duoseptigintillón', ' Duoseptigintillones'],
        [' Un Unseptigintillón', ' Unseptigintillones'], [' Un Septigintillón', ' Septigintillones'],
        [' Un Novensextigintillón', ' Novensextigintillones'], [' Un Octosextigintillón', ' Octosextigintillones'],
        [' Un Septensextigintillón', ' Septensextigintillones'], [' Un Sexvigintillón', ' Sexvigintillones'],
        [' Un Quinsextintillón', ' Quinsextigintillones'], [' Un Cuatorsextigintillón', ' Cuatorsextigintillones'],
        [' Un Tresextigintillón', ' Tresextigintillones'], [' Un Duosextigintillón', ' Duosextigintillones'],
        [' Un Unsextigintillón', ' Unsextigintillones'], [' Un Sextigintillón', ' Sextigintillones'],
        [' Un Novenquintigintillón', ' Novenquintigintillones'], [' Un Octoquintigintillón', ' Octoquintigintillones'],
        [' Un Septenquintigintillón', ' Septenquintigintillones'], [' Un Sexvigintillón', ' Sexvigintillones'],
        [' Un Quinquintintillón', ' Quinquintigintillones'], [' Un Cuatorquintigintillón', ' Cuatorquintigintillones'],
        [' Un Trequintigintillón', ' Trequintigintillones'], [' Un Duoquintigintillón', ' Duoquintigintillones'],
        [' Un Unquintigintillón', ' Unquintigintillones'], [' Un Quintigintillón', ' Quintigintillones'],
        [' Un Novencuatrigintillón', ' Novencuatrigintillones'], [' Un Octocuatrigintillón', ' Octocuatrigintillones'],
        [' Un Septencuatrigintillón', ' Septencuatrigintillones'], [' Un Sexvigintillón', ' Sexvigintillones'],
        [' Un Quincuatrintillón', ' Quincuatrigintillones'], [' Un Cuatorcuatrigintillón', ' Cuatorcuatrigintillones'],
        [' Un Trecuatrigintillón', ' Trecuatrigintillones'], [' Un Duocuatrigintillón', ' Duocuatrigintillones'],
        [' Un Uncuatrigintillón', ' Uncuatrigintillones'], [' Un Cuatrigintillón', ' Cuatrigintillones'],
        [' Un Noventrigintillón', ' Noventrigintillones'], [' Un Octotrigintillón', ' Octotrigintillones'],
        [' Un Septentrigintillón', ' Septentrigintillones'], [' Un Sextrigintillón', ' Sextrigintillones'],
        [' Un Quintrintillón', ' Quintrigintillones'], [' Un Cuatortrigintillón', ' Cuatortrigintillones'],
        [' Un Tretrigintillón', ' Tretrigintillones'], [' Un Duotrigintillón', ' Duotrigintillones'],
        [' Un Untrigintillón', ' Untrigintillones'], [' Un Trigintillón', ' Trigintillones'],
        [' Un Novenvigintillón', ' Novenvigintillones'], [' Un Octovigintillón', ' Octovigintillones'],
        [' Un Septenvigintillón', ' Septenvigintillones'], [' Un Sexvigintillón', ' Sexvigintillones'],
        [' Un Quinvigintillón', ' Quinvigintillones'], [' Un Cuatorvigintillón', ' Cuatorvigintillones'],
        [' Un Trevigintillón', ' Trevigintillones'], [' Un Duovigintillón', ' Duovigintillones'],
        [' Un Unvigintillón', ' Unvigintillones'], [' Un Vigintillón', ' Vigintillones'],
        [' Un Novendecillón', ' Novendecillones'], [' Un Octodecillón', ' Octodecillones'],
        [' Un Septendecillón', ' Septendecillones'], [' Un Sexdecillón', ' Sexdecillones'],
        [' Un Quindecillón', ' Quindecillones'], [' Un Cuatordecillón', ' Cuatordecillones'],
        [' Un Tredecillón', ' Tredecillones'], [' Un Duodecillón', ' Duodecillones'],
        [' Un Undecillón', ' Undecillones'], [' Un Decillón', ' Decillones'],
        [' Un Nonillón', ' Nonillones'], [' Un Octillón', ' Octillones'], [' Un Septillón', ' Septillones'],
        [' Un Sextillón', ' Sextillones'], [' Un Quintillón', ' Quintillones'], [' Un Cuatrillón', ' Cuatrillones'],
        [' Un Trillón', ' Trillones'], [' Un billón', ' Billones'], [' Un Millón', ' Millones']
    ]

    def __init__(self, x: int):

        cambio = len(str(x)) % 6 == 0
        self.x = str(x) if cambio else ''.join([int(6 - int(len(str(x)) % 6)) * '0', str(x)])
        self.a_letras = self.a_letras()

    def a_letras(self):

        if len(self.x) < 7:
            cero = self.x == '000000'
            return ' Cero' if cero else n6(self.x)[1:]
        else:
            grupos = [(self.x[i:i + 6]) for i in range(0, len(self.x), 6)]
            lrg = len(self.x) // 6 - 1
            final = ''
            for indice, elemento in enumerate(self.base[-lrg:]):
                final += ninf(grupos[indice], v1=elemento[0], v2=elemento[1])
            return ''.join([final, n6(grupos[-1])])[1:]


def main():
    print(Numero(123_456_789 + 1000 + 100 + 1).a_letras.lower())


if __name__ == '__main__':
    main()
