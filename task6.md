# Opciones m2o

En la visita, el campo propiedad no debe permitir crear propiedades nuevas ni abrir su formulario.
El visitante solo se debe de poder elegir de los contactos que ya existen.

# Modelo nuevo de imágenes (realestate.property.image)

Crear el modelo con nombre, imagen, secuencia y propiedad (many2one).
Añadir su seguridad (ACL) y el campo image_ids (one2many) a la propiedad.

# Vista embebida

Añadir las imágenes a la propiedad como vista embebida: listado editable inline (`<list editable="bottom">`) con secuencia (widget handle), nombre e imagen (widget image).

# Vistas relacionadas

En la propiedad, añadir las visitas (visit_ids, one2many) usando una vista de listado "simple" con priority, referenciada con list_view_ref en el contexto del campo.

# Contexto

En esa misma lista embebida de visitas, el usuario por defecto de una visita nueva debe ser el responsable de la propiedad (default_user_id: user_id).

# Dominio

En la vista simple de visitas, el campo usuario solo debe mostrar usuarios internos.

# Deberes

## Opciones m2o

En la incidencia, la propiedad no debe dejar crear ni abrir propiedades.

## Modelo nuevo de incidencia en una propiedad

Modelo nuevo llamado incidencia, one2many de las propiedades: secuencia, nombre, descripción, prioridad (4 niveles, para que el widget de estrellas pinte 3), estado, fecha y hora y usuario asignado.

## Seguridad

Añadir la seguridad del modelo nuevo.

## Vista embebida

Añadirlo como vista embebida (listado editable) en propiedad.

## Contexto

El usuario por defecto de la incidencia debe ser el responsable de la propiedad.

## Dominio

En la vista embebida, el campo usuario solo permite usuarios internos.
