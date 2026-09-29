# Grupos
* El botón "Delete Refused Offers" de la propiedad solo lo debe ver el grupo Manager.
* El botón "Cancel Pending Visits" también solo para Manager.

# Copy
* Al duplicar una propiedad, la referencia no se debe copiar (copy=False): hoy duplicar falla por el unique de reference.
* Al duplicar un contrato, el nombre no se debe copiar (copy=False): mismo error con unique(name).

# Campos avanzados
* Poder archivar propiedades: añadir active a la propiedad.
* Etiquetas: modelo realestate.property.tag (nombre y color) y campo tag_ids (Many2many) en la propiedad con widget="many2many_tags".
* Compañía: añadir company_id a la propiedad (compañía del usuario por defecto) y un campo nuevo company_dependent de notas internas (internal_note).

# Monetary
* Pasar a Monetary el precio de la propiedad, el importe de la oferta y el alquiler/fianza del contrato, con su currency_id y widget="monetary" en las vistas.

# Wizards
* Asistente para cambiar la etapa de manera masiva a las propiedades seleccionadas en el listado (TransientModel + action con binding_model_id y binding_view_types="list", target new).

# Deberes
* Asistente que cree visitas en lote desde la propiedad entre dos fechas (widget daterange), en estado planificado y con el responsable de la propiedad.
* Poder archivar categorías (active en realestate.category).
