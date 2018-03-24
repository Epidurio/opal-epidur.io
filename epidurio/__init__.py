"""
epidurio - A Labour Epidural Management Application built with Opal Framework
"""
from opal.core import application, menus


class Application(application.OpalApplication):
    javascripts   = [
        'js/epidurio/routes.js',
        'js/epidurio/directives.js',
        'js/opal/controllers/discharge.js',
        'js/epidurio/epidural_insertion_ctrl.js',
        'js/epidurio/epidural_request_ctrl.js',
        'js/epidurio/follow_up_ctrl.js',
        'js/epidurio/add_patient.js',
        # Uncomment this if you want to implement custom dynamic flows.
        # 'js/epidurio/flow.js',
    ]

    styles = [
        "css/epidurio.css"
    ]

    @classmethod
    def get_menu_items(klass, user=None):
        items = [
            menus.MenuItem(
                href='/#/list/labour/',
                display="Labour Ward",
                icon="fa-plus-circle",
                activepattern='labour',
                index=1
            ),
            menus.MenuItem(
                href="pathway/#/add_patient/",
                icon="fa fa-female",
                display="Add Patient",
                activepattern="add_patient",
                index=2
            ),
            menus.MenuItem(
                href='/#/list/epidural_requested/',
                display="Epidurals Requested",
                icon="fa-plus-circle",
                activepattern='epidural_requested',
                index=3
            ),
            menus.MenuItem(
                href='/#/list/epidural_completed/',
                display="Follow Ups",
                icon="fa fa-mail-forward",
                activepattern='epidural_completed',
                index=4
            ),
            menus.MenuItem(
                href='/accounts/logout/',
                display="Log Out",
                icon="fa fa-sign-out",
                index=5
            ),
        ]
        return items
