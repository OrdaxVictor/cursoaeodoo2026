from odoo.tests import common


class TestRealEstateProperty(common.TransactionCase):

    def setUp(self):
        super().setUp()
        self.Property = self.env['realestate.property']
        self.Visit = self.env['realestate.visit']
        self.Offer = self.env['realestate.offer']

        self.property_1 = self.Property.create({
            'name': 'Test Property 1',
            'price': 100000.0,
        })
        self.visit_1 = self.Visit.create({
            'property_id': self.property_1.id,
            'date': '2024-06-01 10:00:00',
            'status': 'S'
        })
        self.visit_2 = self.Visit.create({
            'property_id': self.property_1.id,
            'date': '2024-06-02 10:00:00',
            'status': 'P'
        })
        self.visit_3 = self.Visit.create({
            'property_id': self.property_1.id,
            'date': '2024-06-03 10:00:00',
            'status': 'P'
        })

        self.offer_1 = self.Offer.create({
            'property_id': self.property_1.id,
            'offer': 95000.0,
            'status': 'S'
        })

        self.offer_2 = self.Offer.create({
            'property_id': self.property_1.id,
            'offer': 97000.0,
            'status': 'S'
        })

    def test_action_create_visit(self):
        self.property_1.action_create_visit()
        self.assertEqual(len(self.property_1.visit_ids), 4)

    def test_action_accept_best_offer(self):
        self.property_1.action_accept_best_offer()
        self.assertEqual(self.offer_2.status, 'A')
        self.assertEqual(self.offer_1.status, 'S')
        self.assertFalse(self.property_1.availability)
        self.assertTrue(self.offer_2.offer > self.offer_1.offer)