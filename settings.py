from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS,
# it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps
# as self.session.config,
# e.g. self.session.config['participation_fee']

# MTurk

AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')

mturk_hit_settings = {
    'keywords': ['bonus', 'study'],
    'title': 'Economic experiment',
    'description': 'This is an economic experiment where you will be forming a group with two other persons. Your payoff will be determined by your decision and the decision of the others.',
    'frame_height': 500,
    'preview_template': 'global/MTurkPreview.html',
    'minutes_allotted_per_assignment': 10,
    'expiration_hours': 24,  # 7 days
    # 'grant_qualification_id': 'YOUR_QUALIFICATION_ID_HERE',
    # to prevent retakes
    'qualification_requirements': []
}

# Session configuration


SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': .01,
    'participation_fee': 1.00,
    'doc': "",
    'mturk_hit_settings': mturk_hit_settings,
}

SESSION_CONFIGS = [
    {
       'name': 'trust_simple_three',
       'display_name': "Team production",
       'num_demo_participants': 3,
       'app_sequence': ['trust_simple_three'],
    },

]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    {
        'name': 'econ_class',
        'display_name': 'Experimental Economics Classroom Lab',
    },
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '1ebp@l7azdagx*94cxayz5o6v2r-1s+v7e#q90q@ry^w_@++7+'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = [
    'otree',
]


EXTENSION_APPS = []
