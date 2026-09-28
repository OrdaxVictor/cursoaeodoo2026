# Constraint
* Añadir un constraint en la oferta para que el importe no pueda ser negativo.
* Añadir restricción SQL en la que la referencia de la propiedad sea única.

# Onchange
* En la visita, cambiar el teléfono y el email: quitar el related y añadir un onchange para que cuando se cambie el contacto se traigan el teléfono y el email.

# Actions
* Hacer un smartbutton para que en la propiedad aparezcan las visitas asociadas a esa propiedad.

# Default
* La propiedad cuando se cree, que tenga un usuario asignado.
* Cuando se cree un contrato que se ponga la fecha de hoy como fecha de inicio.

# Cron
* Cron que busque los contratos en progreso de manera diaria, si la fecha de fin ha pasado, el estado se pondrá a finalizado.

# Deberes
* Un constraint en el contrato que impida que la fecha de fin sea anterior a la fecha de inicio.
* Restricción SQL en el nombre del contrato, que sea único.
* Un onchange en el contrato: al elegir la propiedad, que el alquiler se rellene con el precio de la propiedad.
* Hacer un smartbutton para que en la propiedad aparezcan las incidencias asociadas.
* Cuando se cree una visita, que la fecha por defecto sea la de ahora.
* Cron que busque las visitas planificadas y las ponga en done si su fecha ya ha pasado.
