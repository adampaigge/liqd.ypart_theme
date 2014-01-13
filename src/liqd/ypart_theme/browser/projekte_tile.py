from plone.tiles import PersistentTile
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class ProjekteTile(PersistentTile):

    template = ViewPageTemplateFile('projekte_tile.pt')

    def __call__(self):
        self.description = self.data.get('description', u'')
        self.teaserl_description = self.data.get('teaserl_description', u'')
        self.teaserl_title = self.data.get('teaserl_title', u'')
        self.teaserr_description = self.data.get('teaserr_description', u'')
        self.teaserr_title = self.data.get('teaserr_title', u'')
        return self.template()
