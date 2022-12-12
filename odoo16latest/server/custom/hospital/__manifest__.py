{
    'name': "Hospital Management",
    'version': '1.0',
    'depends': ['base', 'mail','sale'],
    'author': "kholoud",
    'category': 'Extra Tools',
    'summary': 'Hospital Management module',
    'sequence': '2',
    'description': """ This is my first module""",
    'company': 'kholoud',
    'website': ' ',
    'description': """
    This is hospital management customization module
    """,

    # data files always loaded at installation
    'data': [
        'view/patientview.xml',
        'data/sequence.xml',
        'security/ir.model.access.csv'
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
    ],

    'images': ['static/description/icon.png'],

    'installable': True,
    'auto_install': False,
    'application': True,



}