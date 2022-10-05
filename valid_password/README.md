# Ejercicio de un validador de contraseñas

La gracia de este ejercicio fue que los requerimientos fueron de a uno, por lo que cada nuevo requerimiento requeria bastante refactor al codigo y a los tests.

### Requerimientos
#### Regla de Negocio Nº1: longitud mínima de 8 caracteres.
Si no se cumple, debe retornar False y el mensaje "La password debe contener al menos 8 caracteres"

#### Regla de Negocio Nº2: la password debe contener al menos 2 números.
Si no se cumple, debe retornar False y el mensaje "La password debe contener al menos 2 números"

#### Regla de Negocio Nº3: la función de validación debe poder manejar múltiples errores de validación.
Por ejemplo: "mipass" debería retornar el mensaje "La password debe contener al menos 8 caracteres\nLa password debe contener al menos 2 números"

#### Regla de Negocio Nº4: la password debe contener al menos una letra mayúscula.
Si no se cumple, debe retornar False y el mensaje "La password debe contener al menos una letra mayúscula"

#### Regla de Negocio Nº5: la password debe contener al menos un caracter especial.
Si no se cumple, debe retornar False y el mensaje "La password debe contener al menos un caracter especial"