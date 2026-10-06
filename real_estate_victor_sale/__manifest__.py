# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Real Estate Víctor Sale',
    'version': '1.0',
    'summary': 'Real Estate Management',
    'description': 'Module for managing real estate sales',
    'author': 'Víctor',
    'category': 'Real Estate',
    'depends': ['real_estate_victor','sale'],
    'data': [
        'views/realestate_contract_view.xml',
        'views/sale_order_view.xml',
    ],
    'installable': True,
}