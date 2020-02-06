# Numlet

Numlet es una pequeña librería basada en Python capaz de convertir más de 10^600 diferentes números naturales y cero a letras.

## Instalación
### Paso 1:
[Descarga](https://github.com/roylanmartinez/Numlet/archive/master.zip) el zip del repostorio
### Paso 2:
Dentro del zip del repositorio, navega a ***Numlet-master/numlet*** donde encontrarás el archivo ***numlet.py***
### Paso 3:
Copias el archivo ***numlet.py*** y lo pegas en el mismo directorio de tu script.
## Uso
Ahora en tu script simplemente lo importas.
```python
import numlet as nl
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
