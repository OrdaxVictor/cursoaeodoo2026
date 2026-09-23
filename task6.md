# Opciones m2o

En la visita no se debe de poder crear propiedades nuevas ni abrir su formulario.
El visitante solo se debe de poder elegir de los contactos que ya existen.

# Modelo nuevo de incidencia en una propiedad

Vamos a crear un modelo nuevo llamado incidencia. Este modelo va a ser un one2many para las propiedades.

Va a tener un campo de secuencia, nombre, descripción, prioridad, un estado, un campo fecha y hora y un usuario asignado.

# Seguridad

Añadir la seguridad del modelo nuevo.

# Vista embebida

Vamos a añadir este modelo como vista embebida (listado editable) en propiedad.

# Contexto

Vamos a decir desde contexto, que el campo por defecto de usuario de la incidencia sea el responsable de la propiedad.

# Dominio

En la vista embebida de incidencias, añadir un dominio al campo usuario para que solo se puedan asignar usuarios internos.
