# Numlet

Numlet es una pequeña librería basada en Python capaz de convertir más de 10^600 diferentes números naturales y cero a letras.

## Instalación

Descarga el archivo [numlet.py](https://github.com/roylanmartinez/Numeros-naturales-y-cero-a-letras/tree/master/numlet/) y guardalo en el mismo directorio de tu python script.

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
   Repositorio: https://github.com/roylanmartinez/Numeros-naturales-y-cero-a-letras
