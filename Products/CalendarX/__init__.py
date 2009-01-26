from Products.CMFCore.DirectoryView import registerDirectory
import sys

ADD_CONTENT_PERMISSION = 'Add portal content'
PROJECTNAME='CalendarX'

registerDirectory('skins', globals())
calendarxGlobals=globals()
this_module = sys.modules[ __name__ ]

def initialize(context):
    import CalendarXFolder
    from Products.CMFCore import utils

    contentClasses = ( CalendarXFolder.CalendarXFolder , )
    contentConstructors = ( CalendarXFolder.addCalendarXFolder, )
    ftis = ( CalendarXFolder.factory_type_information, )

    utils.ContentInit( 'CalendarX Content'
                     , content_types=contentClasses
                     , permission=ADD_CONTENT_PERMISSION
                     , extra_constructors=contentConstructors
                     , fti=ftis
                     ).initialize( context )


# fixing the 'lines' property for CMF FSPropertiesObject
from Products.CMFCore.FSPropertiesObject import FSPropertiesObject
from Products.CMFCore.DirectoryView import expandpath
from OFS.Folder import Folder
from ZPublisher.Converters import get_converter

def _createZODBClone(self):
    """Create a ZODB (editable) equivalent of this object."""
    # Create a Folder to hold the properties.
    obj = Folder()
    obj.id = self.getId()
    map = []
    for p in self._properties:
        # This should be secure since the properties come
        # from the filesystem.
        setattr(obj, p['id'], getattr(self, p['id']))
        if not p['type'] in ('selection','multiple selection'):
            map.append({'id': p['id'],
                        'type': p['type'],
                        'mode': 'wd',})
        else:
            map.append({'id': p['id'],
                        'type': p['type'],
                        'mode': 'wd',
                        'select_variable': p['select_variable'],})
        #map.append({'id': p['id'],
        #            'type': p['type'],
        #            'mode': 'wd',})
    obj._properties = tuple(map)
    return obj

def _readFile(self, reparse):
    """Read the data from the filesystem.

    Read the file (indicated by exandpath(self._filepath), and parse the
    data if necessary.  Added multilines for lines and text attributes.
    Multiline properties are denoted in file with an integer trailing the
    "=" sign, representing mlinescount (= num of following lines to read).
    Also added code to allow use of selection and multiple selection.
    """
    #list of property types that require multiline creation.
    #extend these lists if new multiline properties added to Converters.py
    multilineproplist = ['lines','ulines','text','utext']
    listtypes = ['lines','ulines'] #convert to lists before Converters

    fp = expandpath(self._filepath)

    file = open(fp, 'r')    # not 'rb', as this is a text file!
    try:
        lines = file.readlines()
    finally:
        file.close()

    map = []
    lino=0
    mlflag = 0            #flag set during a multiline read
    mlinescount = 0       #num lines in the multiline read
    mlinenum = 0          #counter set during a multiline read
    mlfinish = 0          #flag set at end of a multiline read

    for line in lines:

        lino = lino + 1
        linetest = line.strip()

        if not mlflag and (not linetest or linetest[0] == '#'):
            continue

        try:
            if mlflag:      # gather multilines into propvstr
                propvstr = propvstr + line
                if mlinenum == mlinescount:
                    mlflag = 0
                    mlfinish = 1
                    if propvstr[-1] == '\n':
                        propvstr = propvstr[:-1]  #chop off final newline
                        if proptype in listtypes:
                            propvstr = propvstr.split('\n')  #make a list
                else:
                    mlinenum = mlinenum + 1
                    continue
            else:           # handles new property info
                line = linetest
                propname, proptv = line.split(':',1)
                proptype, propvstr = proptv.split('=',1)
                propname = propname.strip()
                proptype = proptype.strip()
                propvstr = propvstr.strip()
            if proptype in multilineproplist and not mlfinish:
                mlinescount = int(propvstr)
                propvstr = ''
                mlinenum = 1
                mlflag = 1
                mlfinish = 0
                continue
            mlfinish = 0
            # Should be safe since we're loading from
            # the filesystem.
            if not proptype in ['selection','multiple selection']:
                converter = get_converter( proptype, lambda x: x )
                propvalue = converter( propvstr )
                setattr(self, propname, propvalue)
                map.append({'id':propname,
                            'type':proptype,
                            'mode':'',
                            'default_value':propvalue,
                            })
            else:
                propvalue = propvstr
                setattr(self, propname, propvalue)
                map.append({'id':propname,
                            'type':proptype,
                            'mode':'',
                            'select_variable':propvalue,
                            })
        except:
            raise ValueError, ( 'Error processing line %s of %s:\n%s'
                              % (lino,fp,line) )
    self._properties = tuple(map)

FSPropertiesObject._createZODBClone = _createZODBClone
FSPropertiesObject._readFile = _readFile
# end of monkey patch

