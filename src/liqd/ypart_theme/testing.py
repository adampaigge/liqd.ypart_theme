import doctest

from zope.configuration import xmlconfig

from plone.testing import z2

from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing.layers import FunctionalTesting
from plone.app.testing.layers import IntegrationTesting

class Liqdypart_ThemeLayer(PloneSandboxLayer):

    def setUpZope(self, app, configurationContext):
        import liqd.ypart_theme
        xmlconfig.file(
            'configure.zcml',
            liqd.ypart_theme,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'liqd.ypart_theme:default')

LIQD_YPART_THEME_FIXTURE = Liqdypart_ThemeLayer()

LIQD_YPART_THEME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(LIQD_YPART_THEME_FIXTURE,),
    name="Liqdypart_ThemeLayer:Integration"
)
LIQD_YPART_THEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(LIQD_YPART_THEME_FIXTURE, z2.ZSERVER_FIXTURE),
    name="Liqdypart_ThemeLayer:Functional"
)
