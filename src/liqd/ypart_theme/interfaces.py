from plone.app.contenttypes.interfaces import IPloneAppContenttypesLayer
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ILiqdYpart_themeLayer( IPloneAppContenttypesLayer):
    """ A layer specific to this product.
    this layer is registered using browserlayer.xml in the package
    default GenericSetup profile
    """



class IProjekteViewletMarker(Interface):
    """Market interface to enable the Projekte viewlet"""
