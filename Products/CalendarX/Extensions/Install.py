from Products.CalendarX import calendarxGlobals, PROJECTNAME
from StringIO import StringIO
from Products.CMFCore.utils import getToolByName, minimalpath
from Products.CMFCore.DirectoryView import addDirectoryViews, \
     registerDirectory, manage_listAvailableDirectories
from App.Common import package_home
from Products.CMFCore.TypesTool import FactoryTypeInformation
from os.path import isdir, join
import os

def install_subskin(self, out, globals=calendarxGlobals, product_skins_dir='skins'):
    skinstool=getToolByName(self, 'portal_skins')

    fullProductSkinsPath = os.path.join(package_home(globals), product_skins_dir)
    productSkinsPath = minimalpath(fullProductSkinsPath)
    registered_directories = manage_listAvailableDirectories()
    if productSkinsPath not in registered_directories:
        try:
            registerDirectory(product_skins_dir, globals)
        except OSError, ex:
            if ex.errno == 2: # No such file or directory
                return
            raise
    try:
        addDirectoryViews(skinstool, product_skins_dir, globals)
    except BadRequestException, e:
        pass  # directory view has already been added

    files = os.listdir(fullProductSkinsPath)
    for productSkinName in files:
        if (isdir(join(fullProductSkinsPath, productSkinName))
            and productSkinName != 'CVS'
            and productSkinName != '.svn'):
            for skinName in skinstool.getSkinSelections():
                path = skinstool.getSkinPath(skinName)
                path = [i.strip() for i in  path.split(',')]
                try:
                    if productSkinName not in path:
                        path.insert(path.index('custom') +1, productSkinName)
                except ValueError:
                    if productSkinName not in path:
                        path.append(productSkinName)
                path = ','.join(path)
                skinstool.addSkinSelection(skinName, path)


from Products.CMFCore.utils import getToolByName

def install(self):
    ''' '''
    out = StringIO()
    install_subskin(self, out, calendarxGlobals)

    typesTool=getToolByName(self, 'portal_types')
    if hasattr(typesTool, 'CalendarX'):
        typesTool._delObject('CalendarX')
    typesTool.manage_addTypeInformation(FactoryTypeInformation.meta_type,
                                        id='CalendarX',
                                        typeinfo_name='CalendarX: CalendarX')

    print >> out, "Successfully installed %s." % PROJECTNAME
    return out.getvalue()
