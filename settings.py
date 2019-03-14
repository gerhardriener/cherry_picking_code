from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS,
# it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps
# as self.session.config,
# e.g. self.session.config['participation_fee']

# Session configuration

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': .30,
    'participation_fee': 1.50,
    'doc': "",
    # 'mturk_hit_settings': mturk_hit_settings,
}

SESSION_CONFIGS = [
    {
       'name': 'trust_simple_three',
       'display_name': "Economic experiment",
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
        'name': 'econ101',
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
