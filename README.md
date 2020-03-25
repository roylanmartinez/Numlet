<div style="padding-top: 15px">
    <a href="LICENSE">
        <img src="https://img.shields.io/badge/license-MIT-brightgreen" /></a>
    <a href="setup.py">
        <img src="https://img.shields.io/badge/version-2.0-informational" /></a>
</div>

# Numlet

Numlet es una pequeña librería basada en Python capaz de convertir más de dos duocentillones de números diferentes a letras. 

## Instrucciones de instalación 
###### Pero antes,
 - Asegurate de tener la última versión de pip instalada.
 - Nota que la primera alternativa se lleva a cabo desde un archivo normal de Python y la 
 segunda desde un Jupyter Notebook.
#### Primera alternativa.
###### Esta alternativa se ha probado desde PyCharm.
1. Abre el script donde quieres importar Numlet.
2. Ve a la terminal del IDE y ejecuta:
```
    >  pip install git+https://github.com/roylanmartinez/Numlet.git
```
###### Si trabajas desde otro IDE y no sabes como instalar un package haz clíck
 [aquí](https://packaging.python.org/tutorials/installing-packages/)

3. Listo. Ve a la sección [Utilización](#utilización). 

#### Segunda alternativa
###### Esta alternativa se ha probado desde Jupyter Notebook.
1. Abre el script donde quieras importar Numlet.
2. En la primera celda ejecuta:
```
    In []: ! pip install git+https://github.com/roylanmartinez/Numlet.git
```
3. Listo. Ve a la sección [Utilización](#utilización). 
## Utilización 
Ahora en tu script simplemente la importas.
```python
from nlt import numlet as nl
```

##### Ejemplo 1:
```python
n = 1
resultado = nl.Numero(n).a_letras
print(resultado)
```
> Uno
##### Ejemplo 2:
```python
n = -1000.123
resultado = nl.Numero(n).a_letras.lower()
print(resultado)
```
 > menos mil con ciento veintitrés milésimas
##### Ejemplo 3: 
###### *Recuerda poner los números décimales muy pequeños en comillas, más información [aquí](https://docs.python.org/3/tutorial/floatingpoint.html)*
```python
n = '0.0000000000000000001'
resultado = nl.Numero(n).a_letras.upper()
print(resultado)
```
> CERO CON UNA DIEZTRILLONÉSIMA
##### Ejemplo 4:
```python
n = -1*abs(1 + 1000 + 1.12)
resultado = nl.Numero(n).a_letras
print(resultado)
```
 > Menos Mil Dos Con Doce Centésimas
## Contribución
Las pull requests son bienvenidas, así como comentarios acerca de mejoras o bugs. 

## Licencia
[MIT](LICENSE)

### ¡Espero que les guste! 
Repositorio: https://github.com/roylanmartinez/Numlet
