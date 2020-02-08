# Numlet

Numlet es una pequeña librería basada en Python capaz de convertir más de 10^600 diferentes números naturales y cero a letras.

## Instrucciones de instalación 
###### Pero antes,
 - Asegurate de tener la última versión de pip instalada.
 - Nota que la primera alternativa se lleva a cabo desde un archivo normal de Python y la segunda desde un Jupyter Notebook.
#### Primera alternativa.
###### Esta alternativa se ha probado desde PyCharm.
##### 1. Abre el script donde quieres importar Numlet.
##### 2. Ve a la terminal del IDE y ejecuta:
    >  pip install git+https://github.com/roylanmartinez/Numlet.git
###### Si trabajas desde otro IDE y no sabes como instalar un package haz clíck [aquí](https://packaging.python.org/tutorials/installing-packages/)

#####3. Listo. Ve a la sección [Utilización](#utilización). 

#### Segunda alternativa
###### Esta alternativa se ha probado desde Jupyter Notebook.
##### 1. Abre el script donde quieras importar Numlet.
##### 2. En la primera celda ejecuta:
```python
In []: ! pip install git+https://github.com/roylanmartinez/Numlet.git
```
#####3. Listo. En la siguiente sección puedes ver como utilizarla.
## Utilización 
Ahora en tu script simplemente lo importas.
```python
from Numlet import numlet as nl
```
###### Sino sabes como importar un módulo haz click [aquí](https://docs.python.org/3/tutorial/modules.html).

##### Ejemplo 1:
```python
n = 1210
resultado = nl.Numero(n).a_letras
print(resultado)
```
> Mil Doscientos Diez
##### Ejemplo 2:
```python
n = 1210
resultado = nl.Numero(n).a_letras.lower()
print(resultado)
```
 > mil doscientos diez
##### Ejemplo 3:
```python
n = abs(-121*10)
resultado = nl.Numero(n).a_letras.upper()
print(resultado)
```
> MIL DOSCIENTOS DIEZ
## Contribución
Las pull requests son bienvenidas, así como comentarios acerca de mejoras o bugs. 

## Licencia
[MIT](LICENSE)

   ### ¡Espero que les guste! 
   Repositorio: https://github.com/roylanmartinez/Numlet
