# Tutoria 5

## Herencia

* Heredar `product.template` y añadir un booleano (p. ej. `is_rental`, "Es de
  alquiler"); añadirlo también a la vista del producto.
* Heredar el botón de confirmar pedido (`action_confirm` de `sale.order`): al
  confirmar un pedido que tenga una línea con un producto de alquiler, crear
  automáticamente un contrato en borrador (cliente, producto e importe del
  alquiler) enlazado al pedido. Si el pedido ya tiene contrato, no crear otro.

