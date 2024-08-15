{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'category': '',
    'author': 'Gregory Goufan',
    'summary': 'Hospital Management System',
    'description': """Hospital Management System""",
    'sequence': -100,
    'depends': ['mail', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'data/patient_tag_data.xml',
        'data/patient.tag.csv',
        'wizard/cancel_appointment_view.xml',
        'views/male_patient_view.xml',
        'views/female_patient_view.xml',
        'views/patient_view.xml',
        'views/appointment_view.xml',
        'views/patient_tag_view.xml',
        'views/menu.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'assets': {},
}
