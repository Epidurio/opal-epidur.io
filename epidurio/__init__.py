"""
epidurio - Our Opal Application
"""
from opal.core import application

class Application(application.OpalApplication):
    javascripts   = [
        'js/epidurio/routes.js',
        'js/opal/controllers/discharge.js',
        'js/epidurio/epidural_insertion_ctrl.js',
        'js/epidurio/epidural_request_ctrl.js',
        'js/epidurio/follow_up_ctrl.js',
        # Uncomment this if you want to implement custom dynamic flows.
        # 'js/epidurio/flow.js',
    ]
