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



@classmethod
def get_menu_items(klass, user=None):

    menuitem = menus.MenuItem(
            href='/epidural_requested/',
            display="Follow Ups",
            icon="fa fa-mail-forward",
            activepattern='epidural_requested',
            index=3
        )

    items.append(menuitem)

    return items
