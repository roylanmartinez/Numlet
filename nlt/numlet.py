"""
   La librería de Numlet te permite convertir más de dos duocentillones de números distintos a letras.
   La clase 'Numeros' toma como parámetro un valor (tipo int o float) y retorna un string mediante el método 'a_letras',
   además on el fin de trabajar números decimales muy largos Numlet también acepta strings y números en notación
   científica.

   Las instrucciones y ejemplos están dentro de la clase Numero.

   ¡Espero que les guste!

   Repositorio: https://github.com/roylanmartinez/Numlet
"""


class Numero:
    """
        Esta clase básicamente controla el uso de las funciones compactadores ninf() y n6(), que a su vez coordinan el
        uso de las funciones base ni(), nni() y nnni(). Además, incluye los datos que posteriormente se ordenan
        y se pasan como parámetros a la propiedad a_letras para dar con el dato facilitado.

           Ejemplos de uso:

        Primer ejemplo:
           n = 1
           resultado = Numero(n).a_letras
           print(resultado)
           --- Uno

        Segundo ejemplo:
            n = -1000.123
            resultado = Numero(n).a_letras.lower()
            print(resultado)
           --- menos mil con ciento veintitrés milésimas

        Tercer ejemplo:
            # recuerda poner los números décimales muy pequeños en comillas, pues el intérprete los trunca.
            Más información: https://docs.python.org/3/tutorial/floatingpoint.html
            n = '0.0000000000000000001'
            resultado = Numero(n).a_letras.upper()
            print(resultado)
           --- CERO CON UNA DIEZTRILLONÉSIMA

        """

    # Instanciador y eliminador de espacios: __init__()
    def __init__(self, numero):
        self.num = self.moldecimal(str(numero).strip())

    base = [
        [' Un Centillón', ' Centillones'],
        [' Un Novenonigintillón', ' Novenonigintillones'], [
            ' Un Octononigintillón', ' Octononigintillones'],
        [' Un Septenonigintillón', ' Septenonigintillones'], [
            ' Un Sexvigintillón', ' Sexvigintillones'],
        [' Un Quinonintillón', ' Quinonigintillones'], [
            ' Un Cuatornonigintillón', ' Cuatornonigintillones'],
        [' Un Trenonigintillón', ' Trenonigintillones'], [
            ' Un Duononigintillón', ' Duononigintillones'],
        [' Un Unonigintillón', ' Unonigintillones'], [
            ' Un Nonigintillón', ' Nonigintillones'],
        [' Un Novenoctigintillón', ' Novenoctigintillones'], [
            ' Un Octooctigintillón', ' Octooctigintillones'],
        [' Un Septenoctigintillón', ' Septenoctigintillones'], [
            ' Un Sexvigintillón', ' Sexvigintillones'],
        [' Un Quinoctintillón', ' Quinoctigintillones'], [
            ' Un Cuatoroctigintillón', ' Cuatoroctigintillones'],
        [' Un Treoctigintillón', ' Treoctigintillones'], [
            ' Un Duooctigintillón', ' Duooctigintillones'],
        [' Un Unoctigintillón', ' Unoctigintillones'], [
            ' Un Octigintillón', ' Octigintillones'],
        [' Un Novenseptigintillón', ' Novenseptigintillones'], [
            ' Un Octoseptigintillón', ' Octoseptigintillones'],
        [' Un Septenseptigintillón', ' Septenseptigintillones'], [
            ' Un Sexvigintillón', ' Sexvigintillones'],
        [' Un Quinseptintillón', ' Quinseptigintillones'], [
            ' Un Cuatorseptigintillón', ' Cuatorseptigintillones'],
        [' Un Treseptigintillón', ' Treseptigintillones'], [
            ' Un Duoseptigintillón', ' Duoseptigintillones'],
        [' Un Unseptigintillón', ' Unseptigintillones'], [
            ' Un Septigintillón', ' Septigintillones'],
        [' Un Novensextigintillón', ' Novensextigintillones'], [
            ' Un Octosextigintillón', ' Octosextigintillones'],
        [' Un Septensextigintillón', ' Septensextigintillones'], [
            ' Un Sexvigintillón', ' Sexvigintillones'],
        [' Un Quinsextintillón', ' Quinsextigintillones'], [
            ' Un Cuatorsextigintillón', ' Cuatorsextigintillones'],
        [' Un Tresextigintillón', ' Tresextigintillones'], [
            ' Un Duosextigintillón', ' Duosextigintillones'],
        [' Un Unsextigintillón', ' Unsextigintillones'], [
            ' Un Sextigintillón', ' Sextigintillones'],
        [' Un Novenquintigintillón', ' Novenquintigintillones'],
        [' Un Octoquintigintillón', ' Octoquintigintillones'],
        [' Un Septenquintigintillón', ' Septenquintigintillones'], [
            ' Un Sexvigintillón', ' Sexvigintillones'],
        [' Un Quinquintintillón', ' Quinquintigintillones'],
        [' Un Cuatorquintigintillón', ' Cuatorquintigintillones'],
        [' Un Trequintigintillón', ' Trequintigintillones'], [
            ' Un Duoquintigintillón', ' Duoquintigintillones'],
        [' Un Unquintigintillón', ' Unquintigintillones'], [
            ' Un Quintigintillón', ' Quintigintillones'],
        [' Un Novencuatrigintillón', ' Novencuatrigintillones'],
        [' Un Octocuatrigintillón', ' Octocuatrigintillones'],
        [' Un Septencuatrigintillón', ' Septencuatrigintillones'], [
            ' Un Sexvigintillón', ' Sexvigintillones'],
        [' Un Quincuatrintillón', ' Quincuatrigintillones'],
        [' Un Cuatorcuatrigintillón', ' Cuatorcuatrigintillones'],
        [' Un Trecuatrigintillón', ' Trecuatrigintillones'], [
            ' Un Duocuatrigintillón', ' Duocuatrigintillones'],
        [' Un Uncuatrigintillón', ' Uncuatrigintillones'], [
            ' Un Cuatrigintillón', ' Cuatrigintillones'],
        [' Un Noventrigintillón', ' Noventrigintillones'], [
            ' Un Octotrigintillón', ' Octotrigintillones'],
        [' Un Septentrigintillón', ' Septentrigintillones'], [
            ' Un Sextrigintillón', ' Sextrigintillones'],
        [' Un Quintrintillón', ' Quintrigintillones'], [
            ' Un Cuatortrigintillón', ' Cuatortrigintillones'],
        [' Un Tretrigintillón', ' Tretrigintillones'], [
            ' Un Duotrigintillón', ' Duotrigintillones'],
        [' Un Untrigintillón', ' Untrigintillones'], [
            ' Un Trigintillón', ' Trigintillones'],
        [' Un Novenvigintillón', ' Novenvigintillones'], [
            ' Un Octovigintillón', ' Octovigintillones'],
        [' Un Septenvigintillón', ' Septenvigintillones'], [
            ' Un Sexvigintillón', ' Sexvigintillones'],
        [' Un Quinvigintillón', ' Quinvigintillones'], [
            ' Un Cuatorvigintillón', ' Cuatorvigintillones'],
        [' Un Trevigintillón', ' Trevigintillones'], [
            ' Un Duovigintillón', ' Duovigintillones'],
        [' Un Unvigintillón', ' Unvigintillones'], [
            ' Un Vigintillón', ' Vigintillones'],
        [' Un Novendecillón', ' Novendecillones'], [
            ' Un Octodecillón', ' Octodecillones'],
        [' Un Septendecillón', ' Septendecillones'], [
            ' Un Sexdecillón', ' Sexdecillones'],
        [' Un Quindecillón', ' Quindecillones'], [
            ' Un Cuatordecillón', ' Cuatordecillones'],
        [' Un Tredecillón', ' Tredecillones'], [
            ' Un Duodecillón', ' Duodecillones'],
        [' Un Undecillón', ' Undecillones'], [' Un Decillón', ' Decillones'],
        [' Un Nonillón', ' Nonillones'], [' Un Octillón',
                                          ' Octillones'], [' Un Septillón', ' Septillones'],
        [' Un Sextillón', ' Sextillones'], [' Un Quintillón',
                                            ' Quintillones'], [' Un Cuatrillón', ' Cuatrillones'],
        [' Un Trillón', ' Trillones'], [' Un billón',
                                        ' Billones'], [' Un Millón', ' Millones']
    ]

    # Bases para intermedios y menores de diez: ni(), nni() y nnni()
    @staticmethod
    def ni(valor: str, bef=True, dec=False) -> str:
        if valor == '1':
            if dec:
                return ' Una' if bef else ' Un'
            else:
                return ' Uno' if bef else ' Un'
        elif valor == '2':
            return ' Dos'
        elif valor == '3':
            return ' Tres'
        elif valor == '4':
            return ' Cuatro'
        elif valor == '5':
            return ' Cinco'
        elif valor == '6':
            return ' Seis'
        elif valor == '7':
            return ' Siete'
        elif valor == '8':
            return ' Ocho'
        elif valor == '9':
            return ' Nueve'
        else:
            # elif x == '0':
            return ''

    # traductor de notación científica.
    @classmethod
    def moldecimal(cls, flt) -> str:
        if 'e' in str(flt):
            str_vals = str(flt).split('e')
            coef, exp, return_val = float(str_vals[0]), int(str_vals[1]), ''
            if int(exp) > 0:
                return_val += str(coef).replace('.', '')
                return_val += ''.join(['0' for _ in range(0,
                                                          abs(exp - len(str(coef).split('.')[1])))])
            elif int(exp) < 0:
                return_val += '0.'
                return_val += ''.join(['0' for _ in range(0, abs(exp) - 1)])
                return_val += str(coef).replace('.', '')
            return return_val
        return flt

    # Formateador de números menores que cien e intermedios de cien: nni()
    @classmethod
    def nni(cls, valor: str, bef=True, dec=False) -> str:
        if valor[0] == '1':
            if valor == '10':
                return ' Diez'
            elif valor == '11':
                return ' Once'
            elif valor == '12':
                return ' Doce'
            elif valor == '13':
                return ' Trece'
            elif valor == '14':
                return ' Catorce'
            elif valor == '15':
                return ' Quince'
            elif valor == '16':
                return ' Dieciséis'
            elif valor == '17':
                return ' Diecisiete'
            elif valor == '18':
                return ' Dieciocho'
            else:
                # elif x == '18':
                return ' Diecinueve'
        elif valor[0] == '2':
            if valor == '20':
                return ' Veinte'
            elif valor == '21':
                return ' Veintiuno' if bef else ' Veintiún'
            elif valor == '22':
                return ' Veintidós'
            elif valor == '23':
                return ' Veintitrés'
            elif valor == '24':
                return ' Veinticuatro'
            elif valor == '25':
                return ' Veinticinco'
            elif valor == '26':
                return ' Veinteséis'
            elif valor == '27':
                return ' Veintisiete'
            elif valor == '28':
                return ' Veintiocho'
            else:
                # elif x == '29':
                return ' Veintinueve'
        elif valor[0] == '3':
            return ''.join([' Treinta', '' if valor[1] == '0' else ''.join([' y', cls.ni(valor[1], bef, dec)])])
        elif valor[0] == '4':
            return ''.join([' Cuarenta', '' if valor[1] == '0' else ''.join([' y', cls.ni(valor[1], bef, dec)])])
        elif valor[0] == '5':
            return ''.join([' Cincuenta', '' if valor[1] == '0' else ''.join([' y', cls.ni(valor[1], bef, dec)])])
        elif valor[0] == '6':
            return ''.join([' Sesenta', '' if valor[1] == '0' else ''.join([' y', cls.ni(valor[1], bef, dec)])])
        elif valor[0] == '7':
            return ''.join([' Setenta', '' if valor[1] == '0' else ''.join([' y', cls.ni(valor[1], bef, dec)])])
        elif valor[0] == '8':
            return ''.join([' Ochenta', '' if valor[1] == '0' else ''.join([' y', cls.ni(valor[1], bef, dec)])])
        elif valor[0] == '9':
            return ''.join([' Noventa', '' if valor[1] == '0' else ''.join([' y', cls.ni(valor[1], bef, dec)])])
        else:
            #  elif x[0] == '0':
            return cls.ni(valor[1], bef, dec)

    # Formateador de números menores que mil e intermedios de mil: nnni()
    @classmethod
    def nnni(cls, valor: str, bef=True, dec=False) -> str:
        if valor[0] == '1':
            if valor[1:] == '00':
                return ' Cien'
            else:
                return ''.join([' Ciento', cls.nni(valor[1:3], bef, dec)])
        elif valor[0] == '2':
            return ''.join([' Doscientos', '' if valor[1:3] == '00' else cls.nni(valor[1:3], bef, dec)])
        elif valor[0] == '3':
            return ''.join([' Trescientos', '' if valor[1:3] == '00' else cls.nni(valor[1:3], bef, dec)])
        elif valor[0] == '4':
            return ''.join([' Cuatrocientos', '' if valor[1:3] == '00' else cls.nni(valor[1:3], bef, dec)])
        elif valor[0] == '5':
            return ''.join([' Quinientos', '' if valor[1:3] == '00' else cls.nni(valor[1:3], bef, dec)])
        elif valor[0] == '6':
            return ''.join([' Seiscientos', '' if valor[1:3] == '00' else cls.nni(valor[1:3], bef, dec)])
        elif valor[0] == '7':
            return ''.join([' Setecientos', '' if valor[1:3] == '00' else cls.nni(valor[1:3], bef, dec)])
        elif valor[0] == '8':
            return ''.join([' Ochocientos', '' if valor[1:3] == '00' else cls.nni(valor[1:3], bef, dec)])
        elif valor[0] == '9':
            return ''.join([' Novecientos', '' if valor[1:3] == '00' else cls.nni(valor[1:3], bef, dec)])
        else:
            # elif x[0] == '0':
            return cls.nni(valor[1:], bef, dec)

    # Compactador de menores de un millon: n6()
    @classmethod
    def n6(cls, valor: str, bef=True, dec=False) -> str:
        if valor == '000000':
            return ''
        elif valor[:3] == '001':
            return ''.join([' Mil', cls.nnni(valor[3:], bef, dec)])
        elif valor[:3] == '000':
            return cls.nnni(valor[3:], bef, dec)
        else:
            return ''.join([cls.nnni(valor[:3], bef=False), ' Mil', cls.nnni(valor[3:], bef, dec)])

    # Compactador de intermedios y tipo de cantidad en singular y plural (v1 y v2): ninf()
    @classmethod
    def ninf(cls, valor: str, v1=' Un Millón', v2=' Millones') -> str:
        if valor == '000000':
            return ''
        elif valor == '000001':
            return v1
        else:
            return ''.join([cls.n6(valor, bef=False, dec=False), v2])

    # Lector general para números enteros: lector()
    def lector(self, numero, dec=False):
        cambio = len(numero) % 6 == 0
        entero = numero if cambio else ''.join(
            [int(6 - int(len(numero) % 6)) * '0', numero]
        )

        if len(entero) < 7:
            cero = entero == '000000'
            return 'Cero' if cero else self.n6(entero, True, dec)[1:]
        else:
            final = ''
            lrg = len(entero) // 6 - 1
            grupos = [(entero[i:i + 6]) for i in range(0, len(entero), 6)]
            for indice, elemento in enumerate(self.base[-lrg:]):
                final += self.ninf(grupos[indice],
                                   v1=elemento[0], v2=elemento[1])
            return ''.join([final, self.n6(grupos[-1], True, dec)])[1:]

    # Lector general para números decimales: lectordcml()
    def lectordcml(self, x):
        if x == '0':
            return ''

        else:
            # limpiador
            nozerosr = x.rstrip('0')
            limpio = nozerosr.lstrip('0')

            if len(nozerosr) < 6:
                r = [
                    'Décimas', 'Centésimas', 'Milésimas', 'Diezmilésimas', 'Cienmilésimas',
                ][len(nozerosr) - 1]

                rplural = r[:-1] if limpio == '1' else r
                return ''.join([' Con ', self.lector(limpio, True), ' ', rplural])

            else:
                posicion = len(nozerosr) // 6
                col = len(nozerosr) - (posicion * 6)
                rplural = 'ésima' if limpio == '1' else 'ésimas'
                inicio = ['', 'Diez', 'Cien', 'Mil', 'Diezmil', 'Cienmil'][col]
                medio = ''.join([inicio, self.base[-posicion]
                                 [1].rstrip('es').strip(), rplural])
                return ''.join([' Con ', self.lector(limpio, True), ' ', medio.capitalize()])

    @property
    def a_letras(self):
        try:
            # Llamador de except
            float(self.num)
            if '.' in self.num:
                # float
                decimal = self.num.split('.')
                d0 = str(int(decimal[0]))
                d1 = decimal[1]
                if d1 == len(d1) * d1[0] and d1[0] == '0':
                    d1 = '0'
                decimal = [d0, d1]
                menos = 'Menos ' if decimal[0][0] == '-' else ''
                return ''.join([menos, self.lector(decimal[0].lstrip('-')), self.lectordcml(decimal[1])])

            else:
                # int
                menos = 'Menos ' if self.num[0] == '-' else ''
                return ''.join([menos, self.lector(str(int(self.num)).lstrip('-'))])

        except ValueError:
            raise ValueError(
                'argumento pasado a Numlet no es entero ni tampoco decimal')
