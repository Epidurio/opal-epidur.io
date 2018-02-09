"""
epidurio - Our Opal Application
"""
from opal.core import application

class Application(application.OpalApplication):
    javascripts   = [
        'js/epidurio/routes.js',
        'js/opal/controllers/discharge.js',
        # Uncomment this if you want to implement custom dynamic flows.
        # 'js/epidurio/flow.js',
    ]