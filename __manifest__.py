{
    'name': 'Stock Evaluation Report',
    'version': '19.0.1.0.0',
    'category': 'Inventory',
    'summary': 'Adds Total Value On Selling Price to Stock Reports',
    'description': """
        This module adds a new column "Total Value On Selling Price" 
        to the Product Stock reports, calculated as Quantity On Hand * Product Selling Price.
    """,
    'depends': ['stock', 'stock_account', 'product'],
    'data': [
        'views/product_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
