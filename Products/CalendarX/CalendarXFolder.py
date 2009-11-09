# -*- coding: utf-8 -*-
# $Id$

"""A folderish object with views for displaying Event contents in calendar form"""

__author__ = 'Lupa Zurven <lupa@zurven.com>'
__docformat__ = 'plaintext'

from Products.CMFCore import permissions
from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from Products.Archetypes.BaseFolder import BaseFolder

from Products.CalendarX.config import *
from Products.CalendarX.helplabels as hl
from Products.CalendarX import CXMessageFactory as _

# Some looong descriptions


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
            description=_(u'help_showHighlightFullEvent'
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
            label=_(u'label_includeReviewStateVisible'
                    default=u"Include 'visible' events"),
            description=_(u'help_includeReviewStateVisible'
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
            label=_(u'label_listOfSubjects'
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
            label=-(u'label_eventTypes',
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
                    default=u"Subject Icons")
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
            label="Show Pop Subject",
            description="Whether to show the Subject of the event",
            i18n_domain="CalendarX"
            ),
        schemata="Pop up Properties",
	),

    BooleanField(
        name='showPOPStart',
        widget=BooleanWidget(
            label="Show Pop Start",
            description="Whether to show the Start date and time of the event",
            i18n_domain="CalendarX"
            ),
        schemata="Pop up Properties",
        default=False
	),

    BooleanField(
        name='showPOPEnd',
        widget=BooleanWidget(
            label="Show Pop End",
            description="Whether to show the End date and time of event",
            i18n_domain="CalendarX"
            ),
        schemata="Pop up Properties",
        default=False
	),

    BooleanField(
        name='showPOPCreator',
        widget=BooleanWidget(
            label="Show Pop Creator",
            description="Whether to show the Creator (Plone username) for this event",
            i18n_domain="CalendarX"
            ),
        schemata="Pop up Properties",
        default=False
	),

    BooleanField(
        name='showPOPCreated',
        widget=BooleanWidget(
            label="Show Pop Created",
            description="Whether to show the Created date of the event",
            i18n_domain="CalendarX"
            ),
        schemata="Pop up Properties",
        default=False
	),

    BooleanField(
        name='showPOPModified',
        widget=BooleanWidget(
            label="Show Pop Modified",
            description="Whether to show the Modified date of the event, when the last time this event was edited",
            i18n_domain="CalendarX"
            ),
        schemata="Pop up Properties",
        default=False
	),

    BooleanField(
        name='showPOPState',
        widget=BooleanWidget(
            label="Show Pop State",
            description="Whether to show the review State of the event, such as published, visible, etc.",
            i18n_domain="CalendarX"
            ),
        schemata="Pop up Properties",
        default=False
	),

    BooleanField(
        name='showPOPDescription',
        default=True,
        widget=BooleanWidget(
            label="Show Pop Description",
            description="Whether to show the Description of the event",
            i18n_domain="CalendarX"
            ),
        schemata="Pop up Properties",
	),

    ## Add Event Link Properties (CX_props_addeventlink) ##

    BooleanField(
        name='showAddEventLink',
        widget=BooleanWidget(
            label="Show Add Event Link?",
            description="Check this to include an Add New Event link in the SubjectLinks bar. Controls for this link are below.	 If more than one of the boolean controls below are checked, the ones below will take priority over the ones above.	 For example, if both useANEFolder and useRolesAndFolders are checked, but the current user does not have one of the specified Roles, then the link target will fall back to the specified ANEFolderPath.  The order of these priorities is determined by the code in the Python script getAddNewEventURL.	If no match is found, then a blank string will be returned to the macro, and a condition there will cause NO Add New Event link to be shown.  This way you can restrict display of this link to only certain users or to users with certain roles.	The first two choices (useMemberFolder and useANEFolder) are shown to all Authenticated users, if selected.",
            i18n_domain="CalendarX"
            ),
        schemata='Add Event Link Properties',
        default=False
	),

    BooleanField(
        name='useCreateObjectOnClick',
        widget=BooleanWidget(
            label="Use Create Object On Click",
            description="Together, these two properties tell the link to instantiate a new Event object in the target folder.  Check this if you want to have the link automatically initiate editing of a new event for the user.	Uncheck this property if you want the Add New Event link to simply take the user to a target folder without starting a new Event object automatically.",
            i18n_domain="CalendarX"
            ),
        schemata='Add Event Link Properties',
        default=True
	),

    StringField(
        name='createObjectOnClickCommand',
        widget=StringWidget(
            label="Create Object On Click Command",
            description="The createObjectOnClickCommand string is the command that is carried in the query string of the link's URL target if you are using the useCreateObjectOnClick property.  The default string is: createObject?type_name=Event which will create a new Event object in the target folder of the link. If you have a different event type that you would like to create, replace the meta_name Event with the appropriate meta_name of your desired event type. If you use this feature, it is advisable to also set your portal to use the portal_factory for initiating Events, so that if a user clicks on the link to start a new event but then decides not to finish it, the event will not be abandoned half-finished.	 Portal_factory will simply create a temporary version and then delete it if left unfinished by the user.",
            i18n_domain="CalendarX"
            ),
        schemata='Add Event Link Properties',
	),

    BooleanField(
        name='useMemberFolder',
        widget=BooleanWidget(
            label="Use Member Folder",
            description="Check this so that the link will take users to their default Member folder where they can add Events. *WARNING* If your users do not have a default Member folder, or if it is located somewhere funny (not in mysite/Members/username) then this option may cause an error for your users.",
            i18n_domain="CalendarX"
            ),
        schemata='Add Event Link Properties',
        default=True
	),

    BooleanField(
        name='useMemberSubfolder',
        widget=BooleanWidget(
            label="Use Member Subfolder",
            description="NOTE: ONLY WORKS IF THERE EXISTS A MEMBER'S HOME FOLDER: THERE IS NONE BY DEFAULT IN PLONE 3.0+.  Check this property if you want events to be instantiated in a subfolder of a user's Member folder.  For example, if all your users are musicians in bands (or groupies perhaps) and they post their band gigs on the calendar, then you might want all the events to be saved in a specific subfolder, such as /Members/username/gigs.",
            i18n_domain="CalendarX"
            ),
        schemata='Add Event Link Properties',
        default=False
	),

    StringField(
        name='memberSubfolderPath',
        widget=StringWidget(
            label="Member Subfolder Path",
            description="NOTE: ONLY WORKS IF THERE EXISTS A MEMBER'S HOME FOLDER: THERE IS NONE BY DEFAULT IN PLONE 3.0+.  The proper format for the target folder is relative to the /Members/username folder and should start with a slash, e.g.: /gigs NOTE:  ONLY use this if you are certain that users WILL have the named subfolder in their user folder.	Otherwise it will return 404, page not found error, or default to a folder of this name in the portal root, which is not perhaps what you were wanting.",
            i18n_domain="CalendarX"
            ),
        schemata='Add Event Link Properties',
        default="/subfoldername"
	),

    BooleanField(
        name='useANEFolder',
        widget=BooleanWidget(
            label="Use a Named Folder",
            description="Together, these allow you to specify a single folder that will be the target of the link.",
            i18n_domain="CalendarX"
            ),
        schemata='Add Event Link Properties',
        default=False
	),

    StringField(
        name='ANEFolderPath',
        widget=StringWidget(
            label="Named Folder Path",
            description="The proper format for the target folder is relative to the portal_root and should start with a slash, e.g.: /somefolderintheroot/thefolderforevents",
            i18n_domain="CalendarX"
            ),
        schemata='Add Event Link Properties',
        default="/thecalendar/thefolderofevents"
	),

    BooleanField(
        name='useUsersAndFolders',
        widget=BooleanWidget(
            label="Use Users and Folders",
            description="Together, these allow you to specify a combination of a username and a corresponding single folder that will be the target of the link for that specific user.",
            i18n_domain="CalendarX"
            ),
        schemata='Add Event Link Properties',
        default=False,
	),

    LinesField(
        name='listOfUsersAndFolders',
        widget=LinesWidget(
            label="List of Users and Folders",
            description="The proper format for each line is as follows: username|folderpath where the pipe character (a vertical slash) is used as a separator between the username and folder path.  The proper format for the target folder is relative to the portal_root and should start with a slash, e.g.: /somefolderintheroot/thefolderforevents. An example with two possible role|folder lines: lupa|/calendar/specialevents davos|/calendar/drearyevents If no matching username is found, the priority rules described above will take over to find a suitable target for the user.",
            i18n_domain="CalendarX"
            ),
        schemata='Add Event Link Properties',
        default="",
	),

    BooleanField(
        name='useRolesAndFolders',
        widget=BooleanWidget(
            label="Use Roles and Folders",
            description="Together, these allow you to specify a combination of a Role and a corresponding single folder that will be the target of the link for all users with that Role.",
            i18n_domain="CalendarX"
            ),
        schemata='Add Event Link Properties',
        default=False,
	),

    LinesField(
        name='listOfRolesAndFolders',
        widget=LinesWidget(
            label="List of Roles and Folders",
            description="The proper format for each line is as follows: rolename|folderpath. where the pipe character (a vertical slash) is used as a separator between the role name and folder path.	The proper format for the target folder is relative to the portal_root and should start with a slash, e.g.: /somefolderintheroot/thefolderforevents. An example with two possible role|folder lines: Manager|/calendar/specialevents Member|/calendar/ordinaryevents The lookup stops when a matching role is found for the user.  For example, if the Manager logs in, the link for the Manager will target the folder called specialevents, even though the Manager is also (likely) a Member of the site.  If no matching role is found, the priority rules described above will take over to find a suitable target for the user.",
            i18n_domain="CalendarX"
            ),
        schemata='Add Event Link Properties',
        default="",
	),

    ## Add CSS Properties (CX_props_css) ##

    StringField(
        name='viewTabsBorderColor',
        widget=StringWidget(
            label="View tabs border color",
            description='VIEW: These attributes control aspects of the "view" tabs, (month, week, day, etc. view template names) right at the top where you choose which view of the calendar is showing.  View tabs border color.',
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default="#8cacbb"
	),

    StringField(
        name='viewTabsBackgroundColor',
        widget=StringWidget(
            label="View tabs background color",
            description="View tabs background color",
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default="#dee7ec"
	),

    StringField(
        name='viewFontBaseSize',
        widget=StringWidget(
            label="View tabs font size",
            description="View tabs font size",
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default="95%"
	),

    StringField(
        name='viewFontFamily',
        widget=StringWidget(
            label="View tabs font family",
            description="View tabs font family",
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default='"Lucida Grande", Verdana, Lucida, Helvetica, Arial, sans-serif'
	),

    StringField(
        name='viewTabsFontColor',
        widget=StringWidget(
            label="View tabs font color",
            description="View tabs font color",
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default="#436976"
	),

    StringField(
        name='subjectBarBorderColor',
        widget=StringWidget(
            label="Color of the border around the subject bar",
            description='Subject Bar: These attributes control aspects of the subject bar, where the Private/Public and MetaCalendar Subject choices are found.',
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default="#436976"
	),

    StringField(
        name='subjectBarBackgroundColor',
        widget=StringWidget(
            label="Color of the background for subject bar and My:Public bar",
            description="",
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default="#dee7ec"
	),

    StringField(
        name='subjectFontFamily',
        widget=StringWidget(
            label="Font family for the subject bar and My:Public bar",
            description="",
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default='"Lucida Grande", Verdana, Lucida, Helvetica, Arial, sans-serif'
	),

    StringField(
        name='subjectFontSize',
        widget=StringWidget(
            label="Font size for the subject bar and My:Public bar",
            description="",
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default="97%"
	),

    StringField(
        name='subjectBarFontColor',
        widget=StringWidget(
            label="Font Color for the subject bar and My:Public bar",
            description="",
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default="#436976"
	),

    StringField(
        name='headerCenterFontSize',
        widget=StringWidget(
            label='Header font size (e.g. "July 2009")',
            description='Header: These attributes control aspects of the header area, where the previous and next date arrows, and the calendar date are displayed, at the bottom and top of the calendar.  Code for this is generated in the "prevnextcurrentlinks" macro.',
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default="135%"
	),

    StringField(
        name='headerSideFontSize',
        widget=StringWidget(
            label='"previous" and "next" links font size',
            description="",
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default="93%"
	),

    StringField(
        name='headerFontFamily',
        widget=StringWidget(
            label='Font Family name for "prevnextcurrentlinks" macro',
            description="(prev, next, date header, footer)",
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default='Verdana, Helvetica, Arial, sans-serif'
	),

    StringField(
        name='headerFontColor',
        widget=StringWidget(
            label="Color of the font for header",
            description="(prev, next, date header, footer)",
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default="#436976"
	),

    StringField(
        name='headerHeight',
        widget=StringWidget(
            label='Height added to base for "prevnextcurrentlinks" macro',
            description="(prev, next, date header, footer)",
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default="0px"
	),

    StringField(
        name='headerMarginBottom',
        widget=StringWidget(
            label='Bottom margin pixels for "prevnextcurrentlinks" macro',
            description="(prev, next, date header, footer)",
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default="0px"
	),

    StringField(
        name='headerMarginTop',
        widget=StringWidget(
            label='Top margin pixels for "prevnextcurrentlinks" macro',
            description="(prev, next, date header, footer)",
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default="0px"
	),

    StringField(
        name='headerPadding',
        widget=StringWidget(
            label='Padding size for "prevnextcurrentlinks" macro',
            description="(prev, next, date header, footer)",
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default="3px"
        ),

    StringField(
        name='continuingHeaderFontSize',
        widget=StringWidget(
            label="Continuing events box, header font size",
            description='Continuing: These attributes control aspects of the Continuing Events section, where events that start before or extend across the entire period of view are shown.',
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default="90%"
	),

    StringField(
        name='continuingHeaderFontFamily',
        widget=StringWidget(
            label="Continuing events box, header font family",
            description="",
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default="Verdana, Helvetica, Arial, sans-serif"
	),

    StringField(
        name='continuingOuterBorderColor',
        widget=StringWidget(
            label="Continuing events box, outer border color",
            description="",
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default="#B3CFD9"
	),

    StringField(
        name='continuingOuterBorderWidth',
        widget=StringWidget(
            label="Continuing events box, outer border width",
            description="",
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default="1px"
	),

    StringField(
        name='continuingHeaderBorderColor',
        widget=StringWidget(
            label="Continuing events box, inner border color",
            description="",
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default="#436976"
	),

    StringField(
        name='continuingHeaderBorderWidth',
        widget=StringWidget(
            label="Continuing events box, border width",
            description="",
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default="1px"
	),

    StringField(
        name='continuingHeaderBackgroundColor',
        widget=StringWidget(
            label="Continuing events box, background color",
            description="",
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default="#8CACBB"
	),

    StringField(
        name='continuingRowEventBackgroundColor',
        widget=StringWidget(
            label="Continuing events box, color if an event is present",
            description="",
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default="#DEE7EC"
	),

    StringField(
        name='continuingRowNoEventBackgroundColor',
        widget=StringWidget(
            label="Continuing events box, color if no event",
            description="",
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default="#F7F9FA"
	),

    StringField(
        name='continuingRowHeight',
        widget=StringWidget(
            label="Continuing events box, row height, added to event bottom",
            description="",
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default="5px"
	),

    StringField(
        name='calBorderColor',
        widget=StringWidget(
            label="Main calendar, border color",
            description='Cal: These attributes control aspects of the Main Calendar display.',
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default="#B3CFD9"
	),

    StringField(
        name='calBorderWidth',
        widget=StringWidget(
            label="Main calendar, border width",
            description="",
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default="1px"
	),

    StringField(
        name='calTableRowOddBackgroundColor',
        widget=StringWidget(
            label="Odd row background color for TR tags",
            description="Main calendar, for certain views where odd/even vary in color, this controls the ODD row (in TR tags).",
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default="#F7F9FA"
	),

    StringField(
        name='calTableRowEvenBackgroundColor',
        widget=StringWidget(
            label="Even row background color for TR tags",
            description="Main calendar, for certain views where odd/even vary in color, this controls the EVEN row (in TR tags)",
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default="#DEE7EC"
	),

    StringField(
        name='calTableHeaderBackgroundColor',
        widget=StringWidget(
            label="Background color for TH tags",
            description="Main calendar, TH tags background color.",
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default="#8CACBB"
	),

    StringField(
        name='calTableHeaderBorderColor',
        widget=StringWidget(
            label="Border color for TH tags",
            description="Main calendar,  TH tags border color.",
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default="#436976"
	),

    StringField(
        name='calTableHeaderBorderWidth',
        widget=StringWidget(
            label="Border width for TH tags",
            description="Main calendar,  TH tags border width.",
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default="1px"
	),

    StringField(
        name='calTableHeaderFontColor',
        widget=StringWidget(
            label="Font color for TH tags",
            description="Main calendar,  TH tags font color.",
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default="#FFFFFF"
	),

    StringField(
        name='calEventFontSize',
        widget=StringWidget(
            label="Event font size",
            description="Main calendar, font size for the event listings.",
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default="85%"
	),

    StringField(
        name='calEventFontFamily',
        widget=StringWidget(
            label="Event font family",
            description="Main calendar, font family for the event listings.",
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default="Verdana, Helvetica, Arial, sans-serif"
	),

    StringField(
        name='calEventPendingTextColor',
        widget=StringWidget(
            label="Pending event text color",
            description='Main calendar, text color for the pending event listings.',
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default='#436976'
	),

    StringField(
        name='calEventPrivateTextColor',
        widget=StringWidget(
            label="Private event text color",
            description='Main calendar, text color for the private event listings.',
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default='#821513'
	),

    StringField(
        name='calEventPublishedTextColor',
        widget=StringWidget(
            label="Published event text color",
            description='Main calendar, text color for the published event listings.',
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default='#466A06'
	),

    StringField(
        name='calEventVisibleTextColor',
        widget=StringWidget(
            label="Visible event text color",
            description='Main calendar, text color for the visible event listings.',
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default='#436976'
	),

    StringField(
        name='calTableDataFontColor',
        widget=StringWidget(
            label="Font color for daily calendar cell",
            description='Main calendar, TD tag text color, but is overridden by other CSS rules, mainly.',
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default='#000000'
	),

    StringField(
        name='calTableDataBorderColor',
        widget=StringWidget(
            label="Border color for daily calendar cell",
            description='Main calendar, TD tag border color.',
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default='#DEE7EC'
	),

    StringField(
        name='calTableDataBorderWidth',
        widget=StringWidget(
            label="Border width for daily calendar cell",
            description='Main calendar, TD tag border width.',
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default='1px'
	),

    StringField(
        name='calTableDataNoEventBackgroundColor',
        widget=StringWidget(
            label="Background color for daily calendar cell with no event",
            description='Main calendar, color when a cell has NO EVENT.',
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default='#F7F9FA'
	),

    StringField(
        name='calTableDataEventBackgroundColor',
        widget=StringWidget(
            label="Background color for daily calendar cell with Events",
            description="Main calendar, color when a cell has an EVENT.  Also used in calendar.js.dtml for rollover highlighting return value.",
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default="#DEE7EC"
	),

    StringField(
        name='calTableDataOutOfMonthBackgroundColor',
        widget=StringWidget(
            label="Background color for out-of-month calendar cell",
            description='Main calendar, in the MONTH view when the day shown is NOT a part of the month, this controls the background color.  Also used in calendar.js.dtml for rollover highlighting return value.',
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default='#FFFFFF'
	),

    StringField(
        name='calTableDataOutOfMonthBorderColor',
        widget=StringWidget(
            label="Border color for out-of-month calendar cell",
            description='Main calendar, in the MONTH view when the day shown is NOT a part of the month, this controls the border color.',
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default='#F7F9FA'
	),

    StringField(
        name='calTableDataOutOfMonthBorderWidth',
        widget=StringWidget(
            label="Border width for out-of-month calendar cell",
            description='Main calendar, in the MONTH view when the day shown is NOT a part of the month, this controls the border width.',
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default='1px'
	),

    StringField(
        name='calTableDataSpanDayFontColor',
        widget=StringWidget(
            label="Font color for date in month view daily calendar cell",
            description='Main calendar, in the MONTH view, text color of the date (ie., "3" on June 3 cell).',
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default='#000000'
	),

    StringField(
        name='calTableDataHeightMonthView',
        widget=StringWidget(
            label="Empty height of daily calendar cell in Month view",
            description='Main calendar, in the MONTH view, this controls the empty height of a daily cell.',
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default='105px'
	),

    StringField(
        name='calTableDataHeightDayView',
        widget=StringWidget(
            label="Empty height of daily calendar cell in Day view",
            description='Main calendar, in the DAY view, this controls the empty height of a daily cell.',
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default='35px'
	),

    StringField(
        name='calTableDataHeightWeekbydayView',
        widget=StringWidget(
            label="Empty height of daily calendar cell in WeekByDay view",
            description='Main calendar, in the WEEKBYDAY view, this controls the empty height of a daily cell.',
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default='105px'
	),

    StringField(
        name='calTableDataHeightWeekbyhourView',
        widget=StringWidget(
            label="Empty height of daily hour cell in WeekByHour view",
            description='Main calendar, in the WEEKBYHOUR view, this controls the empty height of a daily cell.',
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default='30px'
	),

    StringField(
        name='calTableDataFontSizeHour',
        widget=StringWidget(
            label="Font size for hour in daily calendar cell",
            description='Main calendar, in the DAY and WEEKBYHOUR views, this controls the font size of the HOUR displayed (ie., "8am" or "13:00")',
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default='130%'
	),

    StringField(
        name='calTableDataEventHighlightBackgroundColor',
        widget=StringWidget(
            label="Background color for event rollover in daily calendar cell",
            description='Main calendar, in the view when an event has a mouseover (rollover) event, this controls the rollover background color.  Read into calendar.js.dtml for this control.',
            i18n_domain="CalendarX"
            ),
        schemata='CSS Properties',
        default='#FFE7C4'
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
    __implements__ = (BaseFolder.__implements__, (),)

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
