from zope.interface import Interface
from zope.schema import (
    Text,
    TextLine,
    URI,
)
from Products.CMFCore.interfaces._content import IDublinCore


class ILiqdYpart_themeLayer(Interface):
    """ A layer specific to this product.
    this layer is registered using browserlayer.xml in the package
    default GenericSetup profile
    """

class IProjekteTileData(Interface):

    description = Text(title=u'Gemeinsamer Einleitungstext',
                       default=u'',
                       required=False)
    teaserl_title = TextLine(title=u'Titel linker Teaser',
                             default=u'youthpart national')
    teaserl_description = Text(title=u'Einleitungstext linker Teaser',
                               default=u"Hier findest du alle Projekt auf"
                               u" nationaler Ebene.")

    teaserl_link = URI(title=u"Link rechter Teaser",
                       required=True)
    teaserr_title = TextLine(title=u'Titel rechter Teaser',
                             default=u'')
    teaserr_description = Text(title=u'Einleitungstext rechter Teaser',
                               default=u"Hier findest du alle Projekt auf"
                               u" nationaler Ebene.")
    teaserr_link = URI(title=u"Link rechter Teaser",
                       required=True,
                       )


class IProjekteViewletMarker(Interface):
    """Market interface to enable the Projekte viewlet"""
