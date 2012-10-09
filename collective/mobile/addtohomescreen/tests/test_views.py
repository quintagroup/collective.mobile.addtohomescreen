""" Module dedicated to test views.py """

import unittest2 as unittest

from zope.component import getMultiAdapter, getUtility

from Products.CMFCore.utils import getToolByName
from plone.app.testing import TEST_USER_NAME, TEST_USER_ID
from plone.app.testing import login
from plone.app.testing import setRoles
from plone.registry.interfaces import IRegistry

from collective.mobile.addtohomescreen.tests.base import INTEGRATION_TESTING
from collective.mobile.addtohomescreen.interfaces import \
                                                  IAddToHomeScreenSettings


def setupAllowedUrlPath(allowed_url_path):
    registry = getUtility(IRegistry) 
    screen_settings = registry.forInterface(IAddToHomeScreenSettings) 
    screen_settings.allowed_url_paths.append(allowed_url_path)


def resetAllowedUrlPaths():
    registry = getUtility(IRegistry) 
    screen_settings = registry.forInterface(IAddToHomeScreenSettings) 
    screen_settings.allowed_url_paths = []


class TestAddToHomeScreenAllowed(unittest.TestCase):
    """ Class dedicated to test class AddToHomeScreenAllowed """

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.portal.REQUEST

        # set ACTUAL_URL to prevent KeyError in class
        # AddToHomeScreenAllowed
        self.request.set('ACTUAL_URL', self.request['URL'])

    def tearDown(self):
        resetAllowedUrlPaths()

    def getObjectPathById(self, obj_id):
        obj = self.portal[obj_id]
        portal_url = getToolByName(obj, 'portal_url')
        obj_path = portal_url.getRelativeUrl(obj)
        return '/' + obj_path

    def createObject(self, obj_type, obj_id):
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        login(self.portal, TEST_USER_NAME)
        return self.portal.invokeFactory(obj_type, id=obj_id)

    def test_browserPath(self):
        """   Method dedicated to test url of object in a browser and 
            checks it in product settings
        """
        # preparing for test
        folder_id = self.createObject('Folder', 'folder-test')
        doc_id = self.createObject('Document', 'doc-test')
        self.request.set('ACTUAL_URL', self.portal[doc_id].absolute_url())

        # set path
        setupAllowedUrlPath('/doc-test')

        # set context for view. The context is not a site root because it
        # has been already tested (test_defaultBehavior)
        addtohomescreen = getMultiAdapter(
            (self.portal[folder_id], self.request),
            name="is_add2homescreen_allowed")

        # check browser path
        self.assertEqual(addtohomescreen(), True)

    def test_defaultBehavior(self):
        """ Method dedicated to test the default behavior of product
        """
        addtohomescreen = getMultiAdapter(
            (self.portal, self.request),
            name="is_add2homescreen_allowed")

        # show add2homeloader.js and add2home.css for site root
        # when allowed_url_paths is empty
        self.assertEqual(addtohomescreen(), True)

    def test_objectPath(self):
        """   Method dedicated to test path of object and 
            checks it in product settings
        """
        # create new document and view for testing
        doc_id = self.createObject('Document', 'doc-test')
        addtohomescreen = getMultiAdapter(
            (self.portal[doc_id], self.request),
            name="is_add2homescreen_allowed")

        # do not show add2homeloader.js and add2home.css for our context
        # if allowed_url_paths is empty
        self.assertEqual(addtohomescreen(), False)
        
        # set path
        setupAllowedUrlPath('/doc-test')
        
        # show add2homeloader.js and add2home.css for our context
        self.assertEqual(addtohomescreen(), True)
        
        # check influence of site id 
        self.portal.id = 'www'
        self.assertEqual(addtohomescreen(), True)

        # show add2homeloader.js and add2home.css for site_root
        # if default page is set
        self.portal.setDefaultPage(doc_id)
        resetAllowedUrlPaths()
        self.assertEqual(addtohomescreen(), True)


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
