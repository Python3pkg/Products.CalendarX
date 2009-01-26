## Script (Python) "getCXAttribute"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=key
##title=key = name of desired attribute
##
"""
Returns an attribute from within the CalendarX default skin property sheets.

mod by lupa for CalendarX-0.4.0(dev)
Released under the GPL (see LICENSE.txt)
key = name of the attribute desired.  REQUIRED.
val = value of the key attribute in one of the CalendarX property sheets
"""
skinslist = getattr(context,'skinSheets','no such sheet list found')
for skin in skinslist:
    skinsheet = getattr(context,skin,'no such skin property sheet found')
    val = getattr(skinsheet,key,'nope')
    if val != 'nope':
        return val
