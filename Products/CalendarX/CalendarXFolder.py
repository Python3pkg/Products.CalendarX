# -*- coding: utf-8 -*-
# $Id$

"""A folderish object with views for displaying Event contents in calendar form"""

__author__ = 'Lupa Zurven <lupa@zurven.com>'
__docformat__ = 'plaintext'

from Products.CMFCore import permissions
from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from Products.Archetypes.BaseFolder import BaseFolder

from Products.SmartColorWidget.Widget import SmartColorWidget

from Products.CalendarX.config import *
from Products.CalendarX import helplabels as hl
from Products.CalendarX import CXMessageFactory as _

FONTNAME_WIDGET_SIZE = 60

schema = Schema((

    IntegerField(
        name='dayOfWeekToStart',
        widget=SelectionWidget(
            label=_(u'label_dayOfWeekToStart', default=u"Day of Week to Start"),
            description=_(u'help_dayOfWeekToStart',
                          default=(u"Value indicates what day of the week"
                                   u" the Month and Week views begin on.")),
            ),
        schemata="Calendar Options",
        vocabulary=[(0, "Sunday"), (1, "Monday"), (2, "Tuesday"),
                    (3, "Wednesday"), (4, "Thursday"), (5, "Friday"),
                    (6, "Saturday",)],
        default=0,
        ),

    StringField(
        name='defaultView',
        widget=StringWidget(
            label=_(u'label_defaultView', default=u"Default view template"),
            description=_(u'help_defaultView',
                          default=(u"Name of the default view to be displayed: "
                                   u"month, weekbyday, weekbyhour, or day.")),
            ),
        schemata="Calendar Options",
        default='month',
        ),

    BooleanField(
        name='useAdvancedQuery',
        widget=BooleanWidget(
            label=_(u'label_useAdvancedQuery', default=u"Use advanced query."),
            description=_(u'help_useAdvancedQuery',
                          default=hl.HELP_USEADVANCEDQUERY)
            ),
        schemata="Calendar Options",
                default=True,
        ),

    StringField(
        name='dayViewStartHour',
        widget=StringWidget(
            label=_(u'label_dayViewStartHour', default=u"Day view start hour"),
            description=_(u'help_dayViewStartHour',
                          default=hl.HELP_DAYVIEWSTARTHOUR),

                ),
        schemata="Calendar Options",
        default=8,
        ),

    StringField(
        name='dayViewEndHour',
        widget=StringWidget(
            label=_(u'label_dayViewEndHour', default=u"Day view end hour"),
            description=_(u'help_dayViewEndHour',
                          default=hl.HELP_DAYVIEWENDHOUR)
            ),
        schemata="Calendar Options",
        default=20,
        ),

    StringField(
        name='earlyDayEventHour',
        widget=StringWidget(
            label=_(u'label_earlyDayEventHour',
                    default=u"Early day event hour"),
            description=_(u'help_earlyDayEventHour',
                          default=hl.HELP_EARLYDAYEVENTHOUR)
            ),
        schemata="Calendar Options",
        default=0,
        ),

    StringField(
        name='hoursDisplay',
        widget=StringWidget(
            label=_(u'label_hoursDisplay', default=u"Hours Display"),
            description=_(u'help_hoursDisplay', default=hl.HELP_HOURSDISPLAY)
            ),
        schemata="Calendar Options",
        default='12ampm',
        ),


    BooleanField(
        name='useHalfHours',
        widget=BooleanWidget(
            label=_(u'label_useHalfHours', default="Use half hours."),
            description=_(u'help_useHalfHours', default=hl.HELP_USEHALFHOURS)
            ),
        schemata="Calendar Options",
        default=False,
        ),

    StringField(
        name='numMonthsForMultiMonthView',
        widget=StringWidget(
            label=_(u'label_numMonthsForMultiMonthView',
                    default=u"Number of months to display in the multi-month view."),
            description=_(u'help_numMonthsForMultiMonthView',
                          default=hl.HELP_NUMMONTHSFORMULTIMONTHVIEW)
            ),
        schemata="Calendar Options",
        default='3'
        ),

    BooleanField(
        name='showHeaderTitleAndIcons',
        widget=BooleanWidget(
            label=_(u'label_showHeaderTitleAndIcons',
                    default=u"Show header title and icons."),
            description=_(u'help_showHeaderTitleAndIcons',
                          default=hl.HELP_SHOWHEADERTITLEANDICONS)
            ),
        schemata="Calendar Options",
        default=False,
        ),

    BooleanField(
        name='showHighlightFullEvent',
        widget=BooleanWidget(
            label=_(u'label_showHighlightFullEvent',
                    default=u"Show full event highlight"),
            description=_(u'help_showHighlightFullEvent',
                          default=hl.HELP_SHOWHILIGHTFULLEVENT)
            ),
        schemata="Calendar Options",
        default=False,
        ),

    BooleanField(
        name='showJumpToDateWidget',
        widget=BooleanWidget(
            label=_(u'label_showJumpToDateWidget',
                    default=u"Show jump-to-date widget"),
            description=_(u'helpshowJumpToDateWidget',
                          default=hl.HELP_SHOWJUMPTODATEWIDGET)
            ),
        schemata="Calendar Options",
        default=True,
        ),

    BooleanField(
        name='useNumericMonthInJumpToDateWidget',
        widget=BooleanWidget(
            label=_(u'label_useNumericMonthInJumpToDateWidget',
                    default=u"Use numeric month in jump-to-date widget"),
            description=_(u'help_useNumericMonthInJumpToDateWidget',
                          default=hl.HELP_USENUMERICMONTHINJUMPTODATEWIDGET)
            ),
        schemata="Calendar Options",
        default=False
        ),

    BooleanField(
        name='showPublicPrivateLink',
        widget=BooleanWidget(
            label=_(u'label_showPublicPrivateLink',
                    default=u"Show public/private link"),
            description=_(u'help_showPublicPrivateLink',
                          default=hl.HELP_SHOWPUBLICPRIVATELINK)
            ),
        schemata="Calendar Options",
        default=False
        ),

    BooleanField(
        name='useMultiSubjects',
        widget=BooleanWidget(
            label=_(u'label_useMultiSubjects',
                    default=u"Use multiple subjects"),
            description=_(u'help_useMultiSubjects',
                          default=hl.HELP_USEMULTISUBJECTS)
            ),
        schemata="Calendar Options",
        default=True,
        ),

    BooleanField(
        name='showSubjectBar',
        widget=BooleanWidget(
            label=_(u'label_showSubjectBar', default=u"Show subject bar"),
            description=_(u'help_showSubjectBar',
                          default=hl.HELP_SHOWSUBJECTBAR)
            ),
        schemata="Calendar Options",
        default=True
        ),

    BooleanField(
        name='useCalendarHelp',
        widget=BooleanWidget(
            label=_(u'label_useCalendarHelp', default=u"Use calendar help"),
            description=_(u'help_useCalendarHelp',
                          default=hl.HELP_USECALENDARHELP)
            ),
        schemata="Calendar Options",
        default=False
        ),

    BooleanField(
        name='includeReviewStateVisible',
        widget=BooleanWidget(
            label=_(u'label_includeReviewStateVisible',
                    default=u"Include 'visible' events"),
            description=_(u'help_includeReviewStateVisible',
                          default=hl.HELP_INCLUDEREVIEWSTATEVISIBLE)
            ),
        schemata="Calendar Options",
        default=True
        ),

    BooleanField(
        name='showPendingLink',
        widget=BooleanWidget(
            label=_(u'label_showPendingLink', default=u"Show pending link"),
            description=_(u'help_showPendingLink',
                          default=hl.HELP_SHOWPENDINGLINK)
            ),
        schemata="Calendar Options",
        default=False
        ),

    BooleanField(
        name='showPrivateEventsToGroupMembers',
        widget=BooleanWidget(
            label=_(u'showPrivateEventsToGroupMembers',
                    default="Show private events to group members"),
            description=_(u'helpshowPrivateEventsToGroupMembers',
                          default=hl.HELP_SHOWPRIVATEEVENTSTOGROUPMEMBERS)
            ),
        schemata="Calendar Options",
        default=False
        ),

    LinesField(
        name='listOfReviewStatesDisplayed',
        widget=LinesWidget(
            label=_(u'label_listOfReviewStatesDisplayed',
                    default="List of review states to be displayed"),
            description=_(u'help_listOfReviewStatesDisplayed',
                          default=hl.HELP_LISTOFREVIEWSTATESDISPLAYED)
            ),
        schemata="Calendar Options",
        # FIXME: this may be computed from workflows associated to event types
        # or from a plone.app.vocabulary.
        default= ('published','external','internal','internally_published'),
        ),

    BooleanField(
        name='showOnlyEventsInMonth',
        widget=BooleanWidget(
            label=_(u'label_showOnlyEventsInMonth',
                    default=u"Show only events in current month"),
            description=_(u'help_showOnlyEventsInMonth',
                          default=hl.HELP_SHOWONLYEVENTSINMONTH)
            ),
        schemata="Calendar Options",
        default=False
        ),

    BooleanField(
        name='labelEventsOnlyAtStart',
        widget=BooleanWidget(
            label=_(u'label_labelEventsOnlyAtStart',
                    default=u"Only label multi-day events on the first day."),
            description=_(u'help_labelEventsOnlyAtStart',
                          default=hl.HELP_LABELEVENTSONLYATSTART)
            ),
        schemata="Calendar Options",
        default=True,
        ),


    LinesField(
        name='listOfSubjects',
        widget=LinesWidget(
            label=_(u'label_listOfSubjects',
                    default=u"List of subjects"),
            description=_(u'help_listOfSubjects',
                          default=hl.HELP_LISTOFSUBJECTS)
            ),
        # FIXME: The widget should provide a list of available subjects.
        schemata="Calendar Options",
        ),

    BooleanField(
        name='restrictToThisListOfSubjects',
        widget=BooleanWidget(
            label=_(u'label_restrictToThisListOfSubjects',
                    default=u"Restrict to this list of subjects"),
            description=_(u'help_restrictToThisListOfSubjects',
                          default=u"Display only those subjects listed above")
            ),
        schemata="Calendar Options",
        default=False
        ),

    LinesField(
        name='eventTypes',
        widget=LinesWidget(
            label=_(u'label_eventTypes',
                    default=u"List of event types"),
            description=_(u'help_eventTypes',
                          default=(u"A list of the portal_types to display "
                                   u"in the calendar."))
            ),
        # FIXME: the list could be retrived from types that implement IEvent, or
        # IATEvent
        schemata="Calendar Options",
        ),

    BooleanField(
        name='restrictToThisListOfTypes',
        widget=BooleanWidget(
            label=_(u'label_restrictToThisListOfTypes',
                    default=u"Restrict to this list of types"),
            description=_(u'help_restrictToThisListOfTypes',
                          default=u"Display only those types listed above")
            ),
        schemata="Calendar Options",
        default=False
        ),

    LinesField(
        name='listOfPaths',
        widget=LinesWidget(
            label=_(u'label_listOfPaths',
                    default=u"List of paths"),
            description=_(u'help_listOfPaths',
                          default=u"A list of the paths to look for events.")
            ),
        # FIXME: use a referencebrowserwidget
        schemata="Calendar Options",
        ),

    BooleanField(
        name='restrictToThisListOfPaths',
        widget=BooleanWidget(
            label=_(u'label_restrictToThisListOfPaths',
                    default=u"Restrict to only these paths"),
            description=_(u'help_restrictToThisListOfPaths',
                          default=(u"Display only events found in the paths "
                                   u"above."))
            ),
        schemata="Calendar Options",
        default=False
        ),

    BooleanField(
        name='restrictToThisFolder',
        widget=BooleanWidget(
            label=_(u'label_restrictToThisFolder',
                    default=u"Restrict to this folder"),
            description=_(u'help_restrictToThisFolder',
                          default=(u"Display only events found within or "
                                   u"beneath the parent folder of this "
                                   "CalendarX instance."))
            ),
        schemata="Calendar Options",
        default=False
        ),

    LinesField(
        name='listOfSubjectTitles',
        widget=LinesWidget(
            label=_(u'label_listOfSubjectTitles',
                     default=u"List of subject titles"),
            description=_(u'help_listOfSubjectTitles',
                          default=(u"Provide a list of shorter titles for "
                                   u"each of your subjects."))
            ),
        schemata="Calendar Options",
        ),

    BooleanField(
        name='useSubjectTitles',
        widget=BooleanWidget(
            label=_(u'label_useSubjectTitles',
                    default=u"Use subject titles"),
            description=_(u'help_useSubjectTitles',
                          default=u"Display the subject title defined above.")
            ),
        schemata="Calendar Options",
        default=False
        ),

    ## Event Display Properties (CX_props_eventdisplays_text) ##

    BooleanField(
        name='useSubjectIcons',
        widget=BooleanWidget(
            label=_(u'label_useSubjectIcons',
                    default=u"Use Subject Icons"),
            description=_(u'help_useSubjectIcons',
                          default=(u"If checked, this will cause the views "
                                   u"to choose an icon for each event based "
                                   u"on the Subject names found in the list."))
            ),
        schemata='Event Display Properties',
        default=False
        ),

    LinesField(
        name='listOfSubjectIcons',
        widget=LinesWidget(
            label=_(u'label_listOfSubjectIcons',
                    default=u"Subject Icons"),
            description=_(u'help_listOfSubjectIcons',
                          default=hl.HELP_LISTOFSUBJECTICONS)
            ),
        schemata='Event Display Properties',
        ),

    BooleanField(
        name='useSubjectCSSClasses',
        widget=BooleanWidget(
            label=_(u'label_useSubjectCSSClasses',
                    default=u"Use Subject CSS Classes"),
            description=_(u'help_useSubjectCSSClasses',
                          default=(u"If checked, this will cause the views to "
                                   u"choose a CSS class for each event based "
                                   u"on the Subject names found in the list."))
            ),
        schemata='Event Display Properties',
        default=False
        ),

    LinesField(
        name='listOfSubjectCSSClasses',
        widget=LinesWidget(
            label=_(u'label_listOfSubjectCSSClasses',
                    default=u"Subject CSS Classes"),
            description=_(u'help_listOfSubjectCSSClasses',
                          default=hl.HELP_LISTOFSUBJECTCSSCLASSES)
            ),
        schemata='Event Display Properties',
        ),

    BooleanField(
        name='useEventTypeIcons',
        widget=BooleanWidget(
            label=_(u'label_useEventTypeIcons',
                    default=u"Use Event Type Icons"),
            description=_(u'help_useEventTypeIcons',
                          default=(u"If checked, this will cause the views to "
                                   u"choose an icon for each event based on "
                                   u"the Event Type (portal_type)."))
            ),
        schemata='Event Display Properties',
        default=False
        ),

    LinesField(
        name='listOfEventTypeIcons',
        widget=LinesWidget(
            label=_(u'label_listOfEventTypeIcons',
                    default=u"Event Type Icons"),
            description=_(u'help_listOfEventTypeIcons',
                          default=hl.HELP_LISTOFEVENTTYPEICONS)
            ),
        schemata='Event Display Properties',
        ),

    BooleanField(
        name='useEventTypeCSSClasses',
        widget=BooleanWidget(
            label=_(u'label_useEventTypeCSSClasses',
                    default=u"Use Event Type CSS Classes"),
            description=_(u'help_useEventTypeCSSClasses',
                          default=(u"If checked, this will cause the views to "
                                   u"choose a CSS class for each event based "
                                   u"on the Event Type (portal_type)."))
            ),
        schemata='Event Display Properties',
        default=False
        ),

    LinesField(
        name='listOfEventTypeCSSClasses',
        widget=LinesWidget(
            label=_(u'label_listOfEventTypeCSSClasses',
                    default=u"Event Type CSS Classes"),
            description=_(u'help_listOfEventTypeCSSClasses',
                          default=hl.HELP_LISTOFEVENTTYPECSSCLASSES)
            ),
        schemata='Event Display Properties',
        ),

    ## End of Event Display Properties ##

    ## Sub Topic Calendar Properties (CX_props_subcalendar_text) ##

    BooleanField(
        name='useSubCalendarSubjectMenu',
        widget=BooleanWidget(
            label=_(u'label_useSubCalendarSubjectMenu',
                    default=u"Sub Calendar Menu"),
            description=_(u'help_useSubCalendarSubjectMenu',
                          default=hl.HELP_USESUBCALENDARSUBJECTMENU)
            ),
        schemata="Sub Calendar Properties",
        default=False
        ),

    LinesField(
        name='listOfSubCalendarIDs',
        widget=LinesWidget(
            label=_(u'label_listOfSubCalendarIDs',
                    default=u"List of SubCalendar IDs"),
            description=_(u'help_listOfSubCalendarIDs',
                          default=(u"For MAIN Calendars: This is a list (one "
                                   u"per line) of the IDs of the subcalendars. "
                                   u"The menu choices uses this list for the "
                                   u"URL links to subcalendars."))
            ),
        # FIXME: Use a reference browser widget
        schemata="Sub Calendar Properties",
        ),

    LinesField(
        name='listOfSubCalendars',
        widget=LinesWidget(
            label=_(u'label_listOfSubCalendars',
                    default=u"List of SubCalendar Names"),
            description=_(u'help_listOfSubCalendars',
                          default=hl.HELP_LISTOFSUBCALENDARS)
                ),
        schemata="Sub Calendar Properties",
        default="",
        ),

    BooleanField(
        name='isSubCalendar',
        widget=BooleanWidget(
            label=_(u'label_isSubCalendar',
                    default=u"Sub Calendar"),
            description=_(u'help_isSubCalendar',
                          default=(u"For SUB Calendars: Check this property if "
                                   u"this CalendarX folder is a subcalendar. "
                                   u"This controls the style of menu displayed "
                                   u"for subcalendars versus non-subcalendars."))
            ),
        schemata="Sub Calendar Properties",
        default=False
        ),

    StringField(
        name='nameOfSubCalendar',
        widget=StringWidget(
            label=_(u'label_nameOfSubCalendar',
                    default=u"Name of Sub Calendar"),
            description=_(u'help_nameOfSubCalendar',
                          default=(u"For SUB Calendars: The name of this "
                                   u"subcalendar. This is displayed in the "
                                   u"Subject Links area on the subcalendar "
                                   u"(and is NOT used on the Main calendar)."))
            ),
        schemata="Sub Calendar Properties",
        ),

    ## End of Sub Calendar Properties (CX_props_subcalendar_text) ##

    BooleanField(
        name='showPOPTitle',
        widget=BooleanWidget(
            label=_(u'label_showPOPTitle',
                    default=u"Show Pop Title"),
            description=_(u'help_showPOPTitle',
                          default=u"Whether to show the Title of the event")
            ),
        schemata="Pop up Properties",
        default=False
        ),

    BooleanField(
        name='showPOPType',
        widget=BooleanWidget(
            label=_(u'label_showPOPType',
                    default=u"Show Pop Type"),
            description=_(
                u'help_showPOPType',
                default=(u"Whether to show the Type string, telling what type "
                         u"of event object is showing up in the calendar"))
            ),
        schemata="Pop up Properties",
        default=False
        ),

    BooleanField(
        name='showPOPSubject',
        default=True,
        widget=BooleanWidget(
            label=_(u'label_showPOPSubject',
                    default=u"Show Pop Subject"),
            description=_(u'help_showPOPSubject',
                          default=u"Whether to show the Subject of the event")
            ),
        schemata="Pop up Properties",
        ),

    BooleanField(
        name='showPOPStart',
        widget=BooleanWidget(
            label=_(u'label_showPOPStart',
                    default=u"Show Pop Start"),
            description=_(
                u'help_showPOPStart',
                default=u"Whether to show the Start date and time of the event"
                )
            ),
        schemata="Pop up Properties",
        default=False
        ),

    BooleanField(
        name='showPOPEnd',
        widget=BooleanWidget(
            label=_(u'label_showPOPEnd',
                    default=u"Show Pop End"),
            description=_(
                u'help_showPOPEnd',
                default=u"Whether to show the End date and time of event"
                )
            ),
        schemata="Pop up Properties",
        default=False
        ),

    BooleanField(
        name='showPOPCreator',
        widget=BooleanWidget(
            label=_(u'label_showPOPCreator',
                    default=u"Show Pop Creator"),
            description=_(
                u'help_showPOPCreator',
                default=(u"Whether to show the Creator (Plone username) for "
                         u"this event")
                )
            ),
        schemata="Pop up Properties",
        default=False
        ),

    BooleanField(
        name='showPOPCreated',
        widget=BooleanWidget(
            label=_(u'label_showPOPCreated',
                    default=u"Show Pop Created"),
            description=_(
                u'help_showPOPCreated',
                default=u"Whether to show the Created date of the event"
                )
            ),
        schemata="Pop up Properties",
        default=False
        ),

    BooleanField(
        name='showPOPModified',
        widget=BooleanWidget(
            label=_(u'label_showPOPModified',
                    default=u"Show Pop Modified"),
            description=_(
                u'help_showPOPModified',
                default=(u"Whether to show the Modified date of the event, "
                         u"when the last time this event was edited")
                )
            ),
        schemata="Pop up Properties",
        default=False
        ),

    BooleanField(
        name='showPOPState',
        widget=BooleanWidget(
            label=_(u'label_showPOPState',
                    default=u"Show Pop State"),
            description=_(
                u'help_showPOPState',
                default=(u"Whether to show the review State of the event, "
                         u"such as published, visible, etc.")
                )
            ),
        schemata="Pop up Properties",
        default=False
        ),

    BooleanField(
        name='showPOPDescription',
        default=True,
        widget=BooleanWidget(
            label=_(u'label_showPOPDescription',
                    default=u"Show Pop Description"),
            description=_(
                u'help_showPOPDescription',
                default=u"Whether to show the Description of the event")
            ),
        schemata="Pop up Properties",
        ),

    ## Add Event Link Properties (CX_props_addeventlink) ##

    BooleanField(
        name='showAddEventLink',
        widget=BooleanWidget(
            label=_(u'label_showAddEventLink',
                    default=u"Show Add Event Link?"),
            description=_(u'help_showAddEventLink',
                          default=hl.HELP_SHOWADDEVENTLINK)
            ),
        schemata='Add Event Link Properties',
        default=False
        ),

    BooleanField(
        name='useCreateObjectOnClick',
        widget=BooleanWidget(
            label=_(u'label_useCreateObjectOnClick',
                    default=u"Use Create Object On Click"),
            description=_(u'help_useCreateObjectOnClick',
                          default=hl.HELP_USECREATEOBJECTONCLICK)
            ),
        schemata='Add Event Link Properties',
        default=True
        ),

    StringField(
        name='createObjectOnClickCommand',
        widget=StringWidget(
            label=_(u'label_createObjectOnClickCommand',
                    default=u"Create Object On Click Command"),
            description=_(u'help_createObjectOnClickCommand',
                          default=hl.HELP_CREATEOBJECTONCLICKCOMMAND)
            ),
        schemata='Add Event Link Properties',
        ),

    BooleanField(
        name='useMemberFolder',
        widget=BooleanWidget(
            label=_(u'label_useMemberFolder',
                    default=u"Use Member Folder"),
            description=_(u'help_useMemberFolder',
                          default=hl.HELP_USEMEMBERFOLDER)
            ),
        schemata='Add Event Link Properties',
        default=True
        ),

    BooleanField(
        name='useMemberSubfolder',
        widget=BooleanWidget(
            label=_(u'label_useMemberSubfolder',
                    default=u"Use Member Subfolder"),
            description=_(u'help_useMemberSubfolder',
                          default=hl.HELP_USEMEMBERSUBFOLDER)
            ),
        schemata='Add Event Link Properties',
        default=False
        ),

    StringField(
        name='memberSubfolderPath',
        widget=StringWidget(
            label=_(u'label_memberSubfolderPath',
                    default="Member Subfolder Path"),
            description=_(u'help_memberSubfolderPath',
                          default=hl.HELP_MEMBERSUBFOLDERPATH)
            ),
        schemata='Add Event Link Properties',
        default="/subfoldername"
        ),

    BooleanField(
        name='useANEFolder',
        widget=BooleanWidget(
            label=_(u'label_useANEFolder',
                    default=u"Use a Named Folder"),
            description=_(
                u'help_useANEFolder',
                default=(u"Together, these allow you to specify a single "
                         u"folder that will be the target of the link.")
                )
            ),
        schemata='Add Event Link Properties',
        default=False
        ),

    StringField(
        name='ANEFolderPath',
        widget=StringWidget(
            label=_(u'label_ANEFolderPath',
                    default=u"Named Folder Path"),
            description=_(
                u'help_ANEFolderPath',
                default=(u"The proper format for the target folder is relative "
                         u"to the portal_root and should start with a slash, "
                         u"e.g.: /somefolderintheroot/thefolderforevents")
                )
            ),
        # FIXME: We should use a reference browser widget for this.
        schemata='Add Event Link Properties',
        default="/thecalendar/thefolderofevents"
        ),

    BooleanField(
        name='useUsersAndFolders',
        Widget=BooleanWidget(
            label=_(u'label_useUsersAndFolders',
                    default=u"Use Users and Folders"),
            description=_(
                u'help_useUsersAndFolders',
                default=(
                    u"Together, these allow you to specify a combination of a "
                    u"username and a corresponding single folder that will be "
                    u"the target of the link for that specific user."
                    )
                )
            ),
        schemata='Add Event Link Properties',
        default=False,
        ),

    LinesField(
        name='listOfUsersAndFolders',
        widget=LinesWidget(
            label=_(u'label_listOfUsersAndFolders',
                    default=u"List of Users and Folders"),
            description=_(u'help_listOfUsersAndFolders',
                          default=hl.HELP_LISTOFUSERSANDFOLDERS)
            ),
        schemata='Add Event Link Properties',
        default="",
        ),

    BooleanField(
        name='useRolesAndFolders',
        widget=BooleanWidget(
            label=_(u'label_useRolesAndFolders',
                    default=u"Use Roles and Folders"),
            description=_(
                u'help_useRolesAndFolders',
                default=(
                    u"Together, these allow you to specify a combination of "
                    u"a Role and a corresponding single folder that will be "
                    u"the target of the link for all users with that Role."
                    )
                )
            ),
        schemata='Add Event Link Properties',
        default=False,
        ),

    LinesField(
        name='listOfRolesAndFolders',
        widget=LinesWidget(
            label=_(u'label_listOfRolesAndFolders',
                    default=u"List of Roles and Folders"),
            description=_(u'help_listOfRolesAndFolders',
                          default=hl.HELP_LISTOFROLESANDFOLDERS)
            ),
        schemata='Add Event Link Properties',
        default="",
        ),

    ## Add CSS Properties (CX_props_css) ##

    StringField(
        name='viewTabsBorderColor',
        widget=SmartColorWidget(
            label=_(u'label_viewTabsBorderColor',
                    default=u"View tabs border color"),
            description=_(
                u'help_viewTabsBorderColor',
                default=(
                    u'VIEW: These attributes control aspects of the "view" '
                    u'tabs, (month, week, day, etc. view template names) right '
                    u'at the top where you choose which view of the calendar '
                    u'is showing.  View tabs border color.'
                    )
                )
            ),
        schemata='CSS Properties',
        default="#8cacbb"
        ),

    StringField(
        name='viewTabsBackgroundColor',
        widget=SmartColorWidget(
            label=_(u'label_viewTabsBackgroundColor',
                    default=u"View tabs background color"),
            description=_(u'help_viewTabsBackgroundColor',
                          default=u"View tabs background color")
            ),
        schemata='CSS Properties',
        default="#dee7ec"
        ),

    StringField(
        name='viewFontBaseSize',
        widget=StringWidget(
            label=_(u'label_viewFontBaseSize',
                    default=u"View tabs font size"),
            description=_(u'help_viewFontBaseSize',
                          default=u"View tabs font size")
            ),
        schemata='CSS Properties',
        # FIWME: use a slider widget
        default="95%"
        ),

    StringField(
        name='viewFontFamily',
        widget=StringWidget(
            label=_(u'label_viewFontFamily',
                    default=u"View tabs font family"),
            description=_(u'help_viewFontFamily',
                          default=u"View tabs font family")
            ),
        schemata='CSS Properties',
        default=DEFAULT_FONTS
        ),

    StringField(
        name='viewTabsFontColor',
        widget=SmartColorWidget(
            label=_(u'label_viewTabsFontColor',
                    default=u"View tabs font color"),
            description=_(u'help_viewTabsFontColor',
                          default=u"View tabs font color")
            ),
        schemata='CSS Properties',
        default="#436976"
        ),

    StringField(
        name='subjectBarBorderColor',
        widget=SmartColorWidget(
            label=_(u'label_subjectBarBorderColor',
                    default=u"Color of the border around the subject bar"),
            description=_(
                u'help_subjectBarBorderColor',
                default=(
                    u'Subject Bar: These attributes control aspects of the '
                    u'subject bar, where the Private/Public and MetaCalendar '
                    u'Subject choices are found.'
                    )
                )
            ),
        schemata='CSS Properties',
        default="#436976"
        ),

    StringField(
        name='subjectBarBackgroundColor',
        widget=SmartColorWidget(
            label=_(u'label_subjectBarBackgroundColor',
                    default=(
                        u"Color of the background for subject bar and "
                        u"My:Public bar"
                        )),
            description=_(u'help_subjectBarBackgroundColor',
                          default=u"")
            ),
        schemata='CSS Properties',
        default="#dee7ec"
        ),

    StringField(
        name='subjectFontFamily',
        widget=StringWidget(
            label=_(u'label_subjectFontFamily',
                    default=(u"Font family for the subject bar and My:Public "
                             u"bar")),
            description=_(u'help_subjectFontFamily',
                          default=u"")
            ),
        schemata='CSS Properties',
        default=DEFAULT_FONTS
        ),

    StringField(
        name='subjectFontSize',
        widget=StringWidget(
            label=_(u'label_subjectFontSize',
                    default=u"Font size for the subject bar and My:Public bar"),
            description=_(u'help_subjectFontSize',
                          default=u"")
            ),
        schemata='CSS Properties',
        default="97%"
        ),

    StringField(
        name='subjectBarFontColor',
        widget=SmartColorWidget(
            label=_(u'label_subjectBarFontColor',
                    default=u"Font Color for the subject bar and My:Public bar"),
            description=_(u'help_subjectBarFontColor',
                          default=u"")
            ),
        schemata='CSS Properties',
        default="#436976"
        ),

    StringField(
        name='headerCenterFontSize',
        widget=StringWidget(
            label=_(u'label_headerCenterFontSize',
                    default=u'Header font size (e.g. "July 2009")'),
            description=_(u'help_headerCenterFontSize',
                          default=hl.HELP_HEADERCENTERFONTSIZE)
            ),
        schemata='CSS Properties',
        default="135%"
        ),

    StringField(
        name='headerSideFontSize',
        widget=StringWidget(
            label=_(u'label_headerSideFontSize',
                    default=u'"previous" and "next" links font size'),
            description=_(u'help_headerSideFontSize',
                          default=u"")
            ),
        schemata='CSS Properties',
        default="93%"
        ),

    StringField(
        name='headerFontFamily',
        widget=StringWidget(
            label=_(
                u'label_headerFontFamily',
                default=(u'Font Family name for "prevnextcurrentlinks" macro')
                ),
            description=_(u'help_headerFontFamily',
                          default=u"(prev, next, date header, footer)")
            ),
        schemata='CSS Properties',
        default=DEFAULT_FONTS
        ),

    StringField(
        name='headerFontColor',
        widget=SmartColorWidget(
            label=_(u'label_headerFontColor',
                    default=u"Color of the font for header"),
            description=_(u'help_headerFontColor',
                          default=u"(prev, next, date header, footer)")
            ),
        schemata='CSS Properties',
        default="#436976"
        ),

    StringField(
        name='headerHeight',
        widget=StringWidget(
            label=_(
                u'label_headerHeight',
                default=u'Height added to base for "prevnextcurrentlinks" macro'
                ),
            description=_(u'help_headerHeight',
                          default=u"(prev, next, date header, footer)")
            ),
        schemata='CSS Properties',
        default="0px"
        ),

    StringField(
        name='headerMarginBottom',
        widget=StringWidget(
            label=_(
                u'label_headerMarginBottom',
                default=u'Bottom margin pixels for "prevnextcurrentlinks" macro'
                ),
            description=_(u'help_headerMarginBottom',
                          default=u"(prev, next, date header, footer)")
            ),
        schemata='CSS Properties',
        default="0px"
        ),

    StringField(
        name='headerMarginTop',
        widget=StringWidget(
            label=_(
                u'label_headerMarginTop',
                default=u'Top margin pixels for "prevnextcurrentlinks" macro'),
            description=_(u'help_headerMarginTop',
                          default=u"(prev, next, date header, footer)")
            ),
        schemata='CSS Properties',
        default="0px"
        ),

    StringField(
        name='headerPadding',
        widget=StringWidget(
            label=_(u'label_headerPadding',
                    default=u'Padding size for "prevnextcurrentlinks" macro'),
            description=_(u'help_headerPadding',
                          default=u"(prev, next, date header, footer)")
            ),
        schemata='CSS Properties',
        default="3px"
        ),

    StringField(
        name='continuingHeaderFontSize',
        widget=StringWidget(
            label=_(u'label_continuingHeaderFontSize',
                    default=u"Continuing events box, header font size"),
            description=_(
                u'help_continuingHeaderFontSize',
                default=(
                    u'Continuing: These attributes control aspects of the '
                    u'Continuing Events section, where events that start '
                    u'before or extend across the entire period of view are '
                    u'shown.'
                    )
                )
            ),
        schemata='CSS Properties',
        default="90%"
        ),

    StringField(
        name='continuingHeaderFontFamily',
        widget=StringWidget(
            label=_(u'label_continuingHeaderFontFamily',
                    default=u"Continuing events box, header font family"),
            description=_(u'help_continuingHeaderFontFamily',
                          default=u"")
            ),
        schemata='CSS Properties',
        default=DEFAULT_FONTS
        ),

    StringField(
        name='continuingOuterBorderColor',
        widget=SmartColorWidget(
            label=_(u'label_continuingOuterBorderColor',
                    default=u"Continuing events box, outer border color"),
            description=_(u'help_continuingOuterBorderColor',
                          default=u"")
            ),
        schemata='CSS Properties',
        default="#b3cfd9"
        ),

    StringField(
        name='continuingOuterBorderWidth',
        widget=StringWidget(
            label=_(u'label_continuingOuterBorderWidth',
                    default=u"Continuing events box, outer border width"),
            description=_(u'help_continuingOuterBorderWidth',
                          default=u"")
            ),
        schemata='CSS Properties',
        default="1px"
        ),

    StringField(
        name='continuingHeaderBorderColor',
        widget=SmartColorWidget(
            label=_(u'label_continuingHeaderBorderColor',
                    default=u"Continuing events box, inner border color"),
            description=_(u'help_continuingHeaderBorderColor',
                          default=u"")
            ),
        schemata='CSS Properties',
        default="#436976"
        ),

    StringField(
        name='continuingHeaderBorderWidth',
        widget=StringWidget(
            label=_(u'label_continuingHeaderBorderWidth',
                    default=u"Continuing events box, border width"),
            description=_(u'help_continuingHeaderBorderWidth',
                          default=u"")
            ),
        schemata='CSS Properties',
        default="1px"
        ),

    StringField(
        name='continuingHeaderBackgroundColor',
        widget=SmartColorWidget(
            label=_(u'label_continuingHeaderBackgroundColor',
                    default=u"Continuing events box, background color"),
            description=_(u'help_continuingHeaderBackgroundColor',
                          default=u"")
            ),
        schemata='CSS Properties',
        default="#8cacbb"
        ),

    StringField(
        name='continuingRowEventBackgroundColor',
        widget=SmartColorWidget(
            label=_(u'label_continuingRowEventBackgroundColor',
                    default=u"Continuing events box, color if an event is present"),
            description=_(u'help_continuingRowEventBackgroundColor',
                          default=u"")
            ),
        schemata='CSS Properties',
        default="#dee7ec"
        ),

    StringField(
        name='continuingRowNoEventBackgroundColor',
        widget=SmartColorWidget(
            label=_(u'label_continuingRowNoEventBackgroundColor',
                    default=u"Continuing events box, color if no event"),
            description=_(u'help_continuingRowNoEventBackgroundColor',
                          default=u"")
            ),
        schemata='CSS Properties',
        default="#f7f9fa"
        ),

    StringField(
        name='continuingRowHeight',
        widget=StringWidget(
            label=_(
                u'label_continuingRowHeight',
                default=(
                    u"Continuing events box, row height, added to event bottom"
                    )
                ),
            description=_(u'help_continuingRowHeight',
                          default=u"")
            ),
        schemata='CSS Properties',
        default="5px"
        ),

    StringField(
        name='calBorderColor',
        widget=SmartColorWidget(
            label=_(u'label_calBorderColor',
                    default=u"Main calendar, border color"),
            description=_(
                u'help_calBorderColor',
                default=(
                    u'Cal: These attributes control aspects of the Main '
                    u'Calendar display.'
                    )
                )
            ),
        schemata='CSS Properties',
        default="#b3cfd9"
        ),

    StringField(
        name='calBorderWidth',
        widget=StringWidget(
            label=_(u'label_calBorderWidth',
                    default=u"Main calendar, border width"),
            description=_(u'help_calBorderWidth',
                          default=u"")
            ),
        schemata='CSS Properties',
        default="1px"
        ),

    StringField(
        name='calTableRowOddBackgroundColor',
        widget=SmartColorWidget(
            label=_(u'label_calTableRowOddBackgroundColor',
                    default=u"Odd row background color for TR tags"),
            description=_(
                u'help_calTableRowOddBackgroundColor',
                default=(
                    u"Main calendar, for certain views where odd/even vary in "
                    u"color, this controls the ODD row (in TR tags)."
                    )
                )
            ),
        schemata='CSS Properties',
        default="#f7f9fa"
        ),

    StringField(
        name='calTableRowEvenBackgroundColor',
        widget=SmartColorWidget(
            label=_(u'label_calTableRowEvenBackgroundColor',
                    default=u"Even row background color for TR tags"),
            description=_(
                u'help_calTableRowEvenBackgroundColor',
                default=(
                    u"Main calendar, for certain views where odd/even vary in "
                    u"color, this controls the EVEN row (in TR tags)"
                    )
                )
            ),
        schemata='CSS Properties',
        default="#dee7ec"
        ),

    StringField(
        name='calTableHeaderBackgroundColor',
        widget=SmartColorWidget(
            label=_(u'label_calTableHeaderBackgroundColor',
                    default=u"Background color for TH tags"),
            description=_(u'help_calTableHeaderBackgroundColor',
                          default=u"Main calendar, TH tags background color.")
            ),
        schemata='CSS Properties',
        default="#8cacbb"
        ),

    StringField(
        name='calTableHeaderBorderColor',
        widget=SmartColorWidget(
            label=_(u'label_calTableHeaderBorderColor',
                    default=u"Border color for TH tags"),
            description=_(u'help_calTableHeaderBorderColor',
                          default=u"Main calendar,  TH tags border color.")
            ),
        schemata='CSS Properties',
        default="#436976"
        ),

    StringField(
        name='calTableHeaderBorderWidth',
        widget=StringWidget(
            label=_(u'label_calTableHeaderBorderWidth',
                    default=u"Border width for TH tags"),
            description=_(u'help_calTableHeaderBorderWidth',
                          default=u"Main calendar,  TH tags border width.")
            ),
        schemata='CSS Properties',
        default="1px"
        ),

    StringField(
        name='calTableHeaderFontColor',
        widget=SmartColorWidget(
            label=_(u'label_calTableHeaderFontColor',
                    default=u"Font color for TH tags"),
            description=_(u'help_calTableHeaderFontColor',
                          default=u"Main calendar,  TH tags font color.")
            ),
        schemata='CSS Properties',
        default="#ffffff"
        ),

    StringField(
        name='calEventFontSize',
        widget=StringWidget(
            label=_(u'label_calEventFontSize',
                    default=u"Event font size"),
            description=_(
                u'help_calEventFontSize',
                default=u"Main calendar, font size for the event listings."
                )
            ),
        schemata='CSS Properties',
        default="85%"
        ),

    StringField(
        name='calEventFontFamily',
        widget=StringWidget(
            label=_(u'label_calEventFontFamily',
                    default=u"Event font family"),
            description=_(
                u'help_calEventFontFamily',
                default=u"Main calendar, font family for the event listings.")
            ),
        schemata='CSS Properties',
        default=DEFAULT_FONTS
        ),

    StringField(
        name='calEventPendingTextColor',
        widget=SmartColorWidget(
            label=_(u'label_calEventPendingTextColor',
                    default=u"Pending event text color"),
            description=_(
                u'help_calEventPendingTextColor',
                default=(u'Main calendar, text color for the pending event '
                         u'listings.')
                )
            ),
        schemata='CSS Properties',
        default='#436976'
        ),


    StringField(
        name='calEventPrivateTextColor',
        widget=SmartColorWidget(
            label=_(u'label_calEventPrivateTextColor',
                    default=u"Private event text color"),
            description=_(
                u'help_calEventPrivateTextColor',
                default=(
                    u'Main calendar, text color for the private event listings.'
                    )
                )
            ),
        schemata='CSS Properties',
        default='#821513'
        ),

    StringField(
        name='calEventPublishedTextColor',
        widget=SmartColorWidget(
            label=_(u'label_calEventPublishedTextColor',
                    default=u"Published event text color"),
            description=_(
                u'help_calEventPublishedTextColor',
                default=(u'Main calendar, text color for the published event '
                         u'listings.')
                )
            ),
        schemata='CSS Properties',
        default='#466a06'
        ),

    StringField(
        name='calEventVisibleTextColor',
        widget=SmartColorWidget(
            label=_(u'label_calEventVisibleTextColor',
                    default=u"Visible event text color"),
            description=_(
                u'help_calEventVisibleTextColor',
                default=(
                    u'Main calendar, text color for the visible event listings.'
                    )
                )
            ),
        schemata='CSS Properties',
        default='#436976'
        ),

    StringField(
        name='calTableDataFontColor',
        widget=SmartColorWidget(
            label=_(u'label_calTableDataFontColor',
                    default=u"Font color for daily calendar cell"),
            description=_(
                u'help_calTableDataFontColor',
                default=(u'Main calendar, TD tag text color, but is overridden '
                         u'by other CSS rules, mainly.')
                )
            ),
        schemata='CSS Properties',
        default='#000000'
        ),

    StringField(
        name='calTableDataBorderColor',
        widget=SmartColorWidget(
            label=_(u'label_calTableDataBorderColor',
                    default=u"Border color for daily calendar cell"),
            description=_(u'help_calTableDataBorderColor',
                          default=u'Main calendar, TD tag border color.')
            ),
        schemata='CSS Properties',
        default='#dee7ec'
        ),

    StringField(
        name='calTableDataBorderWidth',
        widget=StringWidget(
            label=_(u'label_calTableDataBorderWidth',
                    default=u"Border width for daily calendar cell"),
            description=_(u'help_calTableDataBorderWidth',
                          default=u'Main calendar, TD tag border width.')
            ),
        schemata='CSS Properties',
        default='1px'
        ),

    StringField(
        name='calTableDataNoEventBackgroundColor',
        widget=SmartColorWidget(
            label=_(u'label_calTableDataNoEventBackgroundColor',
                    default=(u"Background color for daily calendar cell with"
                             u"no event")),
            description=_(
                u'help_calTableDataNoEventBackgroundColor',
                default=u'Main calendar, color when a cell has NO EVENT.')
            ),
        schemata='CSS Properties',
        default='#f7f9fa'
        ),

    StringField(
        name='calTableDataEventBackgroundColor',
        widget=SmartColorWidget(
            label=_(
                u'label_calTableDataEventBackgroundColor',
                default=u"Background color for daily calendar cell with Events"
                ),
            description=_(
                u'help_calTableDataEventBackgroundColor',
                default=(
                    u"Main calendar, color when a cell has an EVENT.  Also "
                    u"used in calendar.js.dtml for rollover highlighting "
                    u"return value."
                    )
                )
            ),
        schemata='CSS Properties',
        default="#dee7ec"
        ),

    StringField(
        name='calTableDataOutOfMonthBackgroundColor',
        widget=SmartColorWidget(
            label=_(u'label_calTableDataOutOfMonthBackgroundColor',
                    default=u"Background color for out-of-month calendar cell"),
            description=_(
                u'help_calTableDataOutOfMonthBackgroundColor',
                default=(
                    u'Main calendar, in the MONTH view when the day shown is '
                    u'NOT a part of the month, this controls the background '
                    u'color.  Also used in calendar.js.dtml for rollover '
                    u'highlighting return value.'
                    )
                )
            ),
        schemata='CSS Properties',
        default='#ffffff'
        ),

    StringField(
        name='calTableDataOutOfMonthBorderColor',
        widget=SmartColorWidget(
            label=_(u'label_calTableDataOutOfMonthBorderColor',
                    default=u"Border color for out-of-month calendar cell"),
            description=_(
                u'help_calTableDataOutOfMonthBorderColor',
                default=(
                    u'Main calendar, in the MONTH view when the day shown is '
                    u'NOT a part of the month, this controls the border color.'
                    )
                )
            ),
        schemata='CSS Properties',
        default='#f7f9fa'
        ),

    StringField(
        name='calTableDataOutOfMonthBorderWidth',
        widget=StringWidget(
            label=_(u'label_calTableDataOutOfMonthBorderWidth',
                    default=u"Border width for out-of-month calendar cell"),
            description=_(
                u'help_calTableDataOutOfMonthBorderWidth',
                default=(
                    u'Main calendar, in the MONTH view when the day shown is '
                    u'NOT a part of the month, this controls the border width.'
                    )
                )
            ),
        schemata='CSS Properties',
        default='1px'
        ),

    StringField(
        name='calTableDataSpanDayFontColor',
        widget=SmartColorWidget(
            label=_(
                u'label_calTableDataSpanDayFontColor',
                default=u"Font color for date in month view daily calendar cell"
                ),
            description=_(
                u'help_calTableDataSpanDayFontColor',
                default=(
                    u'Main calendar, in the MONTH view, text color of the '
                    u'date (ie., "3" on June 3 cell).')
                )
            ),
        schemata='CSS Properties',
        default='#000000'
        ),

    StringField(
        name='calTableDataHeightMonthView',
        widget=StringWidget(
            label=_(
                u'label_calTableDataHeightMonthView',
                default=u"Empty height of daily calendar cell in Month view"
                ),
            description=_(
                u'help_calTableDataHeightMonthView',
                default=(u'Main calendar, in the MONTH view, this controls the '
                         u'empty height of a daily cell.')
                )
            ),
        schemata='CSS Properties',
        default='105px'
        ),

    StringField(
        name='calTableDataHeightDayView',
        widget=StringWidget(
            label=_(u'label_calTableDataHeightDayView',
                    default=u"Empty height of daily calendar cell in Day view"),
            description=_(
                u'help_calTableDataHeightDayView',
                default=(u'Main calendar, in the DAY view, this controls the '
                         u'empty height of a daily cell.')
                )
            ),
        schemata='CSS Properties',
        default='35px'
        ),

    StringField(
        name='calTableDataHeightWeekbydayView',
        widget=StringWidget(
            label=_(
                u'label_calTableDataHeightWeekbydayView',
                default=(
                    u"Empty height of daily calendar cell in WeekByDay view"
                    )
                ),
            description=_(
                u'help_calTableDataHeightWeekbydayView',
                default=(
                    u'Main calendar, in the WEEKBYDAY view, this controls the '
                    u'empty height of a daily cell.'
                    )
                )
            ),
        schemata='CSS Properties',
        default='105px'
        ),

    StringField(
        name='calTableDataHeightWeekbyhourView',
        widget=StringWidget(
            label=_(
                u'label_calTableDataHeightWeekbyhourView',
                default=u"Empty height of daily hour cell in WeekByHour view"),
            description=_(
                u'help_calTableDataHeightWeekbyhourView',
                default=(u'Main calendar, in the WEEKBYHOUR view, this '
                         u'controls the empty height of a daily cell.')
                )
            ),
        schemata='CSS Properties',
        default='30px'
        ),

    StringField(
        name='calTableDataFontSizeHour',
        widget=StringWidget(
            label=_(u'label_calTableDataFontSizeHour',
                    default=u"Font size for hour in daily calendar cell"),
            description=_(
                u'help_calTableDataFontSizeHour',
                default=(
                    u'Main calendar, in the DAY and WEEKBYHOUR views, this '
                    u'controls the font size of the HOUR displayed (ie., '
                    u'"8am" or "13:00")'
                    )
                )
            ),
        schemata='CSS Properties',
        default='130%'
        ),

    StringField(
        name='calTableDataEventHighlightBackgroundColor',
        widget=SmartColorWidget(
            label=_(u'label_calTableDataEventHighlightBackgroundColor',
                    default=(u"Background color for event rollover in daily "
                             u"calendar cell")),
            description=_(
                u'help_calTableDataEventHighlightBackgroundColor',
                default=(
                    u'Main calendar, in the view when an event has a mouseover '
                    u'(rollover) event, this controls the rollover background '
                    u'color.  Read into calendar.js.dtml for this control.'
                    )
                )
            ),
        schemata='CSS Properties',
        default='#ffe7c4'
        ),

        ## End of Schema Properties  ##

    ),
)

CalendarXFolder_schema = BaseFolder.schema.copy() + schema.copy()

class CalendarXFolder(BaseFolder):
    """CalendarX is a folder (so it can hold other CalendarX subcalendars)
    Based on Archetypes, it has many configurable properties.
    """
    security = ClassSecurityInfo()
    # FIXME: Always use Zope 2 interfaces?
    __implements__ = (BaseFolder.__implements__, (),)

    # FIXME: remove below stuffs already handled by GenericSetup
    # This name appears in the 'add' box
    archetype_name = 'CalendarX'

    meta_type = 'CalendarXFolder'
    portal_type = 'CalendarXFolder'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 1
    content_icon = 'CalendarX16.gif'
    immediate_view = 'showDefaultView'
    default_view = 'showDefaultView'
    suppl_views = ()
    typeDescription = "CalendarXFolder"
    typeDescMsgId = 'description_edit_calendarxfolder'

    # Make sure we get title-to-id generation when an object is created
    _at_rename_after_creation = True

    schema = CalendarXFolder_schema

    aliases = {
        '(Default)'  : 'showDefaultView',
        'index.html' : '(Default)',
        'edit'       : 'base_edit',
        'properties' : 'base_metadata',
        'sharing'    : '',
        'view'       : '(Default)',
        }

registerType(CalendarXFolder, PROJECTNAME)
