from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting


class Fixture(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import collective.mobile.addtohomescreen
        self.loadZCML(package=collective.mobile.addtohomescreen)

    def setUpPloneSite(self, portal):
        # Install the collective.mobile.addtohomescreen product
        self.applyProfile(portal, 'collective.mobile.addtohomescreen:default')


FIXTURE = Fixture()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,),
    name='collective.mobile.addtohomescreen:Integration',
    )
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,),
    name='collective.mobile.addtohomescreen:Functional',
    )
