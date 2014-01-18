from collective.cover.tiles.base import (
    PersistentCoverTile,
    IPersistentCoverTile,
)
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.schema import (
    Text,
    TextLine,
    URI,
)


class IProjekteTileData(IPersistentCoverTile):

    description = Text(title=u'Gemeinsamer Einleitungstext',
                       default=u'',
                       required=False)
    teaserl_title = TextLine(title=u'Titel linker Teaser',
                             default=u'',
                             required=False)
    teaserl_description = Text(title=u'Einleitungstext linker Teaser',
                               default=u"",
                               required=False)

    teaserl_link = URI(title=u"Link rechter Teaser",
                       required=True)
    teaserr_title = TextLine(title=u'Titel rechter Teaser',
                             default=u'',
                             required=False)
    teaserr_description = Text(title=u'Einleitungstext rechter Teaser',
                               default=u"",
                               required=False)
    teaserr_link = URI(title=u"Link rechter Teaser",
                       required=True,
                       )


class ProjekteTile(PersistentCoverTile):

    template = ViewPageTemplateFile('projekte_tile.pt')
    is_configurable = True
    short_name = u'Projekte Tile'

    def __call__(self):
        self.description = self.data.get('description', u'')
        self.teaserl_description = self.data.get('teaserl_description', u'')
        self.teaserl_title = self.data.get('teaserl_title', u'')
        self.teaserl_link = self.data.get('teaserl_link', u'')
        self.teaserr_description = self.data.get('teaserr_description', u'')
        self.teaserr_title = self.data.get('teaserr_title', u'')
        self.teaserr_link = self.data.get('teaserr_link', u'')
        return self.template()
