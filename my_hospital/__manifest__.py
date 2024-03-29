# -*- coding: utf-8 -*-
{
    'name': 'Odoo 15 Development Tutorials',
    'version': '2.0.0',
    'summary': 'Odoo 15 Development Tutorials',
    'sequence': -100,
    'description': """Odoo 15 Development Tutorials""",
    'category': 'Tutorials',
    'author': 'Odoo Mates',
    'maintainer': 'Odoo Mates',
    'website': 'https://www.odoomates.tech',
    'license': 'AGPL-3',
    'depends': [
        'sale',
        'mail',
        'website_slides',
        'hr',
        'product',
    ],
    'data': [
        'security/security_access_data.xml',
        'security/ir.model.access.csv',
        'data/patient_tag_data.xml',
        'data/patient.tag.csv',
        'data/data.xml',
        'data/slide_data_v12.xml',
        'data/slide_data_v13.xml',
        'data/slide_data_v14.xml',
        'data/slide_data_v15.xml',
        # 'wizard/create_appointment_view.xml',
        # 'wizard/search_appointment_view.xml',
        # 'wizard/cancel_appointment_view.xml',
        'views/patient_view.xml',
        'views/doctor_view.xml',
        'views/appointment_view.xml',
        'views/kids_view.xml',
        'views/patient_gender_view.xml',
        'views/sale.xml',
        'views/medical_sections_view.xml',
        'views/patient_tag_view.xml',
        'report/patient_details_template.xml',
        'report/patient_card.xml',
        'report/report.xml'
    ],
    'demo': [],
    'qweb': [],
    'images': ['static/description/banner.gif'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
