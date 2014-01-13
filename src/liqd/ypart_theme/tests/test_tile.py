# -*- coding: utf-8 -*-
from zope.component import queryUtility

from plone.tiles.interfaces import ITileType
import unittest2 as unittest

from plone.app.testing import (
    TEST_USER_ID,
    TEST_USER_NAME,
    setRoles,
    login
)

from plone.registry.interfaces import IRegistry

from liqd.ypart_theme.testing import \
    LIQD_YPART_THEME_INTEGRATION_TESTING


class ProjekteTileIntegrationTest(unittest.TestCase):

    layer = LIQD_YPART_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        login(self.portal, TEST_USER_NAME)
        self.portal.invokeFactory('Document', 'doc')
        self.doc = self.portal.doc

    def test_tile_exists(self):
        from liqd.ypart_theme.browser.projekte_tile import ProjekteTile
        self.assertTrue(ProjekteTile(self.portal, self.request))

    def test_file_rendering(self):
        from liqd.ypart_theme.browser.projekte_tile import ProjekteTile
        self.assertIn("projects_teaser_box",
                      ProjekteTile(self.portal, self.request)())

    def test_tiletype_registration(self):
        self.assertTrue(queryUtility(ITileType, name='liqd.ypart_theme.projekte_tile'))
        self.assertEqual(
            queryUtility(ITileType,
                         name='liqd.ypart_theme.projekte_tile').title,
            "Projekte Teasers")

    def test_tile_registration(self):
        registry = queryUtility(IRegistry)
        self.assertTrue(u'liqd.ypart_theme.projekte_tile'
                        in registry['plone.app.tiles'])


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
