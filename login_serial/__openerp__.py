{
    'name': 'Login Serial',
    'category': 'Login Serial',
    'summary': 'Login Serial',
    'version': '1.0',
    'description':
        '''
    Adds a Serial Id field to the users that can be used to login in without a password.

    A new URL is provided "http://domain/login_serial/" to login with the specified Serial Id.''',
    'author': 'Damian Soriano <ds@ingadhoc.com>',
    'depends': ['website'],
    'external_dependencies':
    {
    },
    'data':
    [
        'views/res_users_view.xml',
        'views/webclient_templates.xml',
    ],
    'installable': True,
}

