# Tutoria 5

## Herencia

* Heredar `product.template` y añadir un booleano (p. ej. `is_rental`, "Es de
  alquiler"); añadirlo también a la vista del producto.
* Heredar el botón de confirmar pedido (`action_confirm` de `sale.order`): al
  confirmar un pedido que tenga una línea con un producto de alquiler, crear
  automáticamente un contrato en borrador (cliente, producto e importe del
  alquiler) enlazado al pedido. Si el pedido ya tiene contrato, no crear otro.

## Mixins

* Añadir chatter a las visitas (`mail.thread` + `mail.activity.mixin` y
  `<chatter/>`), con el estado rastreable.
* Al crear visitas desde el wizard de programar visitas, que quede un mensaje
  en el chatter de cada visita con la propiedad asociada.

## Deberes

* Test del `action_confirm` heredado: pedido con producto de alquiler → se crea
  el contrato.
