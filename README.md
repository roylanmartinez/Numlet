<p align="center">
    <a href="hhttps://github.com/roylanmartinez/Numlet">
        <img src="https://img.shields.io/badge/language-es-brightgreen" /></a>
    <a href="#backers" alt="Backers on Open Collective">
        <img src="https://img.shields.io/badge/status-developed-brightgreen" /></a>
    <a href="hhttps://github.com/roylanmartinez/Numlet">
        <img src="https://img.shields.io/badge/version-1.1-informational" /></a>
    <a href="LICENSE">
        <img src="https://img.shields.io/badge/license-MIT-brightgreen" /></a>
    <a href="FORK">
        <img src="https://img.shields.io/github/forks/roylanmartinez/Numlet?label=Fork&style=social" /></a>
    <a href="https://github.com/roylanmartinez/Numlet/stargazers">
        <img src="https://img.shields.io/github/stars/roylanmartinez/Numlet?style=social" /></a>
    <a href="https://github.com/roylanmartinez/Numlet/stargazers">
        <img src="https://img.shields.io/github/followers/roylanmartinez?label=Follow&style=social" /></a>
</p>

# Numlet

Numlet es una pequeña librería basada en Python capaz de convertir más de 10^600 diferentes números naturales y cero a letras.

## Instrucciones de instalación 
###### Pero antes,
 - Asegurate de tener la última versión de pip instalada.
 - Nota que la primera alternativa se lleva a cabo desde un archivo normal de Python y la segunda desde un Jupyter Notebook.
#### Primera alternativa.
###### Esta alternativa se ha probado desde PyCharm.
1. Abre el script donde quieres importar Numlet.
2. Ve a la terminal del IDE y ejecuta:
```
    >  pip install git+https://github.com/roylanmartinez/Numlet.git
```
###### Si trabajas desde otro IDE y no sabes como instalar un package haz clíck [aquí](https://packaging.python.org/tutorials/installing-packages/)

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
