# Campos calculados

- Con `@api.depends`: duración en días del contrato a partir de la fecha de inicio y la fecha de fin.
- Sin `@api.depends`: días que quedan para que termine el contrato (comparando `end_date` con `fields.Date.today()`). Al no depender de ningún campo, no se puede almacenar.

# Campos relacionales

- En la visita, campo que muestre el teléfono del contacto (related `partner_id.phone`).
- En la oferta, campo que muestre el responsable de la propiedad (related `property_id.user_id`).

# ORM

- `create`: en una propiedad, botón que cree una visita para esa propiedad (fecha y responsable por defecto).
- `search` + `write`: en una propiedad, botón que busque la mejor oferta enviada y la acepte (`order="amount desc"`, `limit=1` + `action_accept`).
- `unlink`: en una propiedad, botón que borre las ofertas rechazadas.

# Deberes

- Campo boolean calculado en el contrato "con fianza" que se ponga a True si la fianza es mayor que 0.
- Campo calculado en el contrato con los días que lleva en curso (hoy menos `start_date`, sin depends).
- Campo relacional en visita que coja el correo electrónico del contacto.
- En una propiedad, botón que cree una oferta en borrador con el importe del precio de la propiedad.
