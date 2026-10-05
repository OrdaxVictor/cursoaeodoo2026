# Herencia

## Modulo original

* Dejar preparado el `button_box` vacio en el formulario del contrato, para poder
  colgarle botones desde el modulo nuevo.

## Modulo nuevo

* Crear el modulo `real_estate_nacho_sale`, que dependa de `sale` y de
  `real_estate_nacho`.

## Herencia por extension

* Añadir al contrato un producto (`product_id`) y un onchange que traiga su precio de
  lista al alquiler.
* En el modulo nuevo, heredar `realestate.contract` y añadirle el one2many de pedidos
  de venta (`order_ids`, inverso de `sale.order.contract_id`), con su contador y su
  smartbutton.
* Heredar el contrato y añadir un boton que cree el pedido de venta: una linea con el
  producto, cantidad 1 y el importe del contrato.
* Heredar `sale.order` y añadirle el contrato asociado (`contract_id`) en la pestaña
  "Other Info".
* Herencia de vistas: colgar el smartbutton dentro del `button_box` del contrato
  (preparado en el modulo original) y añadir el boton y el producto con xpath.

## Herencia de metodos

* Heredar el método `create` del contrato para asignarle el nombre con una secuencia
  (`CTR/2026/00001`).
  Ojo con la compañía de la secuencia: si el usuario es de otra compañía,
  `next_by_code` no la encuentra y el nombre sale vacio.

## Herencia por delegacion

* En el módulo original, crear `realestate.agent` con
  `_inherits = {'res.partner': 'partner_id'}` y probar a añadir a su vista campos de
  `res.partner` (`street`, `city`, `country_id`).
* Añadir `agent_id` a la propiedad y mostrarlo en su formulario.

## Deberes

* Heredar `action_cancelled` del contrato para cancelar sus pedidos de venta.
* Boton en el contrato que confirme los pedidos y cree la factura. (en pedidos el método para crear las facturas en base al pedido es _create_invoices())
* Delegacion en un segundo contacto: `realestate.owner` (propietario) con `_inherits`
  y `owner_id` en la propiedad.
