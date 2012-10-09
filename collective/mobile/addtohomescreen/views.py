""" Module dedicated for views """

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from plone.registry.interfaces import IRegistry
from zope.component import getUtility, getMultiAdapter

from collective.mobile.addtohomescreen.interfaces import \
                                                  IAddToHomeScreenSettings


def lchop(s, start):
    length = len(start)
    if s[:length] == start:
        return s[length:]
    return s

       
class AddToHomeScreenAllowed(BrowserView):
    """ Class dedicated to enable/disable javascript
       (add2homeloader.js) and css styles on the page.
    """
    def __init__(self, context, request):
        self.context = context
        self.request = request

    def getCurrentPaths(self):
        portal_url = getToolByName(self.context, 'portal_url')
        obj_path = portal_url.getRelativeUrl(self.context)
        browser_path = lchop(self.request.ACTUAL_URL, portal_url())
        return ['/' + obj_path, browser_path]

    def isUrlAllowed(self):
        registry = getUtility(IRegistry) 
        screen_settings = registry.forInterface(IAddToHomeScreenSettings) 
        allowed_url_paths = screen_settings.allowed_url_paths

        if allowed_url_paths: 
            obj_path, browser_path = self.getCurrentPaths()
            return (obj_path in allowed_url_paths) or \
                (browser_path in allowed_url_paths) 
        else: 
            return getMultiAdapter(
                (self.context, self.request), 
                name='plone_context_state').is_portal_root()

    def __call__(self):
        return self.isUrlAllowed()
        
       
