# Context

* En el listado de propiedades, que por defecto aparezcan solo las disponibles:
  aplicar el filtro "Available" desde el contexto de la acción
  (`search_default_availability`).
* En el smartbutton de Visitas de la propiedad, que el listado salga filtrado
  por defecto por las visitas programadas: aplicarlo desde el contexto de la acción que
  devuelve el smartbutton (`search_default_...`).

# Mixin

* Añadir chatter al modelo de propiedad: heredar `mail.thread` y
  `mail.activity.mixin`, añadir `mail` a las dependencias del módulo y poner
  `<chatter/>` en el formulario.
* Hacer rastreables en el chatter la etapa (`stage_id`), la disponibilidad y el
  precio; comprobar que cada cambio deja su mensaje.
* Al pulsar algún botón (p. ej. el de reservar la propiedad), enviar un mensaje
  al chatter con `message_post`.

# Tests

Crear los tests en `tests/` sobre `TransactionCase`.

Hacer tests de los siguientes métodos del modelo `realestate.property`:

* `action_create_visit`
* `action_accept_best_offer`

# Deberes

* Añadir chatter también al contrato, con su estado (`state`) rastreable.
* Añadir test al método _compute_next_visit_date
