from datetime import timedelta

from odoo import fields
from odoo.tests import common


class TestNextVisitDate(common.TransactionCase):

    def setUp(self):
        super().setUp()
        self.Property = self.env['realestate.property']
        self.Visit = self.env['realestate.visit']

        self.now = fields.Datetime.now()
        self.property_1 = self.Property.create({
            'name': 'Test Property Next Visit',
        })

    def _create_visit(self, days, status):
        return self.Visit.create({
            'property_id': self.property_1.id,
            'date': self.now + timedelta(days=days),
            'status': status,
        })

    def test_no_visits(self):
        self.assertFalse(self.property_1.next_visit_date)

    def test_earliest_future_scheduled_visit(self):
        self._create_visit(5, 'S')
        visit_soon = self._create_visit(2, 'S')
        self._create_visit(10, 'S')
        self.assertEqual(self.property_1.next_visit_date, visit_soon.date)

    def test_ignores_non_scheduled_visits(self):
        self._create_visit(1, 'P')
        self._create_visit(1, 'V')
        self._create_visit(1, 'C')
        visit_scheduled = self._create_visit(3, 'S')
        self.assertEqual(self.property_1.next_visit_date, visit_scheduled.date)

    def test_ignores_past_scheduled_visits(self):
        self._create_visit(-2, 'S')
        self.assertFalse(self.property_1.next_visit_date)

    def test_recomputes_on_status_change(self):
        visit = self._create_visit(4, 'S')
        self.assertEqual(self.property_1.next_visit_date, visit.date)
        visit.status = 'C'
        self.assertFalse(self.property_1.next_visit_date)

    def test_recomputes_on_date_change(self):
        visit = self._create_visit(4, 'S')
        new_date = self.now + timedelta(days=1)
        visit.date = new_date
        self.assertEqual(self.property_1.next_visit_date, new_date)
