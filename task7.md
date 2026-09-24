# Deberes

## Propiedad: ofertas relacionadas

Añadir a la propiedad el campo `offer_ids` (One2many de `realestate.offer`,
inverso de `property_id`).

## Vista embebida de ofertas

En la propiedad, pestaña "Ofertas" con las ofertas como listado editable inline. Con los campos que queráis.

## Campo calculado 

En la propiedad, `next_visit_date` (Datetime): la fecha de la próxima visita
planificada (la más cercana de sus `visit_ids` en estado planificado). 
Mostrarla en alguna de sus vistas.


## Campo relacionado

En la oferta, campo `category_id` relacionado con la categoría de la propiedad
(`property_id.category_id`), de solo lectura. Añadirlo al formulario.

## Vista kanban de ofertas

Kanban agrupada por estado (`default_group_by="state"`) con tarjeta que muestre
el importe, la propiedad, el comprador y la fecha. Añadir la kanban al `view_mode`
de la action de ofertas.

## Pivot y graph de ofertas

- Pivot: medida importe, fila estado, columna propiedad.
- Graph: barras por estado con el importe como medida.

## Filtros de búsqueda (search) de ofertas

- Búsqueda por escritura en el comprador: que busque por nombre del comprador y
  por nombre de la propiedad, con `filter_domain`:
  `['|', ('partner_id.name', 'ilike', self), ('property_id.name', 'ilike', self)]`
- Filtros: Enviadas, Aceptadas y Rechazadas (por estado).
- Agrupaciones: por estado, por propiedad y por comprador.

## Opciones m2o

- En la oferta, la propiedad no debe dejar crear ni abrir propiedades.
- En el contrato, el inquilino solo se elige entre los contactos existentes (sin poder
  crear contactos desde ahí).

## Dominio

En el contrato, la propiedad solo debe poder ser una propiedad reservada
(`availability = False`).

## ORM

- `create`: en la oferta aceptada, botón que cree un contrato en borrador con esa
  propiedad, ese comprador, tipo venta y fecha de inicio hoy.
- `search` + `write`: en la propiedad, botón que cancele todas sus visitas en
  borrador o planificadas.
