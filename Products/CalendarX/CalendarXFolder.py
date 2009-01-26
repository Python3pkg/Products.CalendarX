from Products.CMFPlone.PloneFolder import PloneFolder, ReplaceableWrapper
from Globals import InitializeClass
try:
    from Products.CMFCore import permissions
except ImportError:
    #BBB Use CMFCorePermissions from CMF 1.4.x (part of Plone 2.0.x) instead.
    from Products.CMFCore import CMFCorePermissions as permissions
from AccessControl import ClassSecurityInfo
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from ComputedAttribute import ComputedAttribute
from Acquisition import aq_base, aq_inner, aq_parent

factory_type_information = { 'id'             : 'CalendarX'
                             , 'meta_type'      : 'CalendarX'
                             , 'description'    : """\
A CalendarX object is a folderish object with a default calendar skin"""
                             , 'icon'           : 'folder_icon.gif'
                             , 'product'        : 'CalendarX'
                             , 'factory'        : 'addCalendarXFolder'
                             , 'filter_content_types' : 0
                             , 'immediate_view' : 'index_html'
                             , 'actions'        :
                                ( { 'id'            : 'view'
                                  , 'name'          : 'View'
                                  , 'action'        : 'string:${folder_url}/'
                                  , 'permissions'   :
                                     (permissions.View,)
                                  , 'category'      : 'folder'
                                  }
                                , { 'id'            : 'local_roles'
                                  , 'name'          : 'Local Roles'
                                  , 'action'        : 'string:${folder_url}/folder_localrole_form'
                                  , 'permissions'   :
                                     (permissions.ManageProperties,)
                                  , 'category'      : 'folder'
                                  }
                                , { 'id'            : 'edit'
                                  , 'name'          : 'Edit'
                                  , 'action'        : 'string:${folder_url}/folder_edit_form'
                                  , 'permissions'   :
                                     (permissions.ManageProperties,)
                                  , 'category'      : 'folder'
                                  }
                                , { 'id'            : 'folderlisting'
                                  , 'name'          : 'Folder Listing'
                                  , 'action'        : 'string:${folder_url}/folder_listing'
                                  , 'permissions'   :
                                     (permissions.View,)
                                  , 'category'      : 'folder'
                                  , 'visible'       : 0
                                  }
                                )
                             }



class CalendarXFolder(PloneFolder):
    security=ClassSecurityInfo()
    meta_type = portal_type = 'CalendarX'

    def __init__(self, id, title=''):
        PloneFolder.__init__(self, id, title)
        self.manage_addProperty('skinSheets',
                                ['CX_props_custom',
                                 'CX_props_calendar',
                                 'CX_props_css',
                                 'CX_props_popup',
                                 'CX_props_addeventlink',
                                 'CX_props_eventdisplays',
                                 'CX_props_subcalendar'],
                                'lines')
        self.manage_addProperty('skinMacros',
                                ['CX_props_macros',],
                                'lines')

    #stolen from PloneFolder
    security.declareProtected('View', 'index_html')
    def index_html(self):
        """ Acquire if not present, and get defaultView from property sheet."""
        props = aq_inner(self).aq_acquire('CX_props_calendar')
        def_view = props.getProperty('defaultView')
#        _target = aq_parent(aq_inner(self)).aq_acquire(def_view)
        _target = aq_inner(self).aq_acquire(def_view)
        return ReplaceableWrapper(aq_base(_target).__of__(self))

    index_html = ComputedAttribute(index_html, 1)

    folder_listing = index_html
    folder_contents = index_html

manage_addCalendarXFolder=CalendarXFolder.manage_addPloneFolder
def addCalendarXFolder( self, id, title='', description='', REQUEST=None ):
    """ adds a Plone Folder """
    sf = CalendarXFolder(id, title=title)
    sf.description=description
    self._setObject(id, sf)
    if REQUEST is not None:
        REQUEST['RESPONSE'].redirect( sf.absolute_url() + '/manage_main' )

InitializeClass(CalendarXFolder)
