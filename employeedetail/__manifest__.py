# -*- coding: utf-8 -*-
{
    'name': "employeedetail",

    'summary': """Manage EmployeeDetails""",

    'description': """
        employeedetail module for maintaining employee details:
            - employee details
            -team
    """,

    'author': "Ram Mani",
    'website': "http://www.devcvare.com",


    'category': 'Test',
    'version': '0.1',


    'depends': ['base'],


    'data': [
        # 'security/ir.model.access.csv',

        'views/employeedetail.xml',

    ],

    'css': ['static/src/css/emp.css'],

    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}