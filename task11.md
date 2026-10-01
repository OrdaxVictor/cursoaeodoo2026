# Tutoria 4


## Acciones

* Smartbutton en la propiedad que abra sus contratos: añadir `contract_ids`
  (One2many, inverso de `property_id`), su contador y el método que devuelva la
  acción con el dominio.

## Wizards

* Acción contextual en el listado de visitas: asistente que cambie el estado de
  todas las visitas seleccionadas (borrador, planificada, hecha o cancelada).
  Ligarlo al listado con `binding_model_id` y `binding_view_types="list"`, como el
  asistente de cambiar etapa de la clase.

## Informe

* Informe PDF de la oferta (`realestate.offer`) con la propiedad, el comprador, el
  importe, la fecha y el estado. Debe salir en el menú Imprimir del listado y del
  formulario.


## Many2many (Esto lo hago yo después)

* En la propiedad, declarar en `tag_ids` su tabla de relación explícita (la que Odoo ya
  generó): `realestate_property_realestate_property_tag_rel`, con
  `column1="realestate_property_id"` y `column2="realestate_property_tag_id"`.
* En la etiqueta (`realestate.property.tag`), crear `property_ids` (Many2many a
  `realestate.property`) como inverso de `tag_ids`: la misma tabla de relación, con
  `column1` y `column2` intercambiados.
* Mostrar `property_ids` en el formulario de la etiqueta.
* Con esto, `tag_ids` y `property_ids` son las dos caras de la misma relación, igual
  que `property_id` (m2o) y `visit_ids` (o2m): asignar o quitar etiquetas desde
  cualquiera de los dos lados mueve la misma tabla.
