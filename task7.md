# Tutoría: repaso y deberes

Repaso de lo visto esta semana: kanban, pivot y graph, campos calculados (con y
sin `depends`), métodos ORM, opciones m2o, vistas embebidas y relaciones, filtros
de búsqueda y dominios.

Los deberes se hacen sobre las ofertas y los contratos, que todavía casi no
tienen vistas, reutilizando todo lo anterior con casos nuevos.

# Deberes

## Propiedad: ofertas relacionadas

Añadir a la propiedad el campo `offer_ids` (One2many de `realestate.offer`,
inverso de `property_id`).

## Vista embebida de ofertas

En la propiedad, pestaña "Ofertas" con las ofertas como listado editable inline
(`<list editable="bottom">`): comprador, importe, fecha y estado
(`widget="badge"` con `decoration-*` por estado).

## Vista relacionada

Crear una vista de formulario reducida y de solo lectura de la propiedad
(referencia, categoría, precio, disponibilidad y responsable) y abrirla desde el
campo propiedad del contrato con `form_view_ref` en el contexto del campo.

## Campo calculado con depends

En la propiedad, `next_visit_date` (Datetime): la fecha de la próxima visita
planificada (la más cercana de sus `visit_ids` en estado planificado),
almacenada (`store=True`). Mostrarla en la lista de propiedades.

## Campo calculado sin depends

En la visita, `days_to_visit` (Integer): los días que quedan hasta la fecha de la
visita. Sin `@api.depends`, por lo que no se puede almacenar. Si no hay fecha, 0.

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
- En el contrato, el inquilino solo se elige entre los contactos existentes (sin
  crear contactos desde ahí).

## Dominio

En el contrato, la propiedad solo debe poder ser una propiedad reservada
(`availability = False`).

## ORM

- `create`: en la oferta aceptada, botón que cree un contrato en borrador con esa
  propiedad, ese comprador, tipo venta y fecha de inicio hoy.
- `search` + `write`: en la propiedad, botón que cancele todas sus visitas en
  borrador o planificadas.
- `unlink`: en la propiedad, botón que borre las imágenes que no tengan foto.
