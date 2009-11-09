# -*- coding: utf-8 -*-
# $Id$
"""Various big help texts too keep AT schema as fit as possible"""

HELP_USEADVANCEDQUERY = u"""If checked, CalendarX will use the AdvancedQuery
product for making queries to the catalog to find events. Use this if you want
to override those query methods in your skin folder. I find AdvancedQuery
significantly easier to use in building complex queries, but it offers no other
advantages for general use in CalendarX.  AdvancedQuery is included with Plone
3."""

HELP_DAYVIEWSTARTHOUR = u"""Hour of day for CalendarX to BEGIN display for day
view and for weekbyhour view. 8 = 8am = 08:00, 20 = 6pm = 20:00. For a 24 hour
calendar, set this to 0 (zero)."""

HELP_DAYVIEWENDHOUR = u"""Hour of day for CalendarX to END display for day
view and for weekbyhour view. 8 = 8am = 08:00, 20 = 6pm = 20:00. For a 24 hour
calendar, set this to 0 (zero)."""

HELP_EARLYDAYEVENTHOUR = u"""Hour of day for CalendarX to use for deciding
between events being classed as "later" or "earlier" in the Day and Weekbyhour
views.  Previous behavior was that events up to midnight showed as "later"
events and "earlier" events from midnight to dayViewStartHour showed up as
"continuing".  This property is the hour that now serves as the boundary between
these types of events.

Default value is 0, representing 12 midnight, meaning there are no "later"
events.  Setting value to 3, will represent 3am.  Seems a reasonable boundary to
me, meaning that events running 1am-2am will show up on the previous day, say
Saturday night instead of Sunday morning.

Use Case: Calendar of events for a city where there are commonly late night
movies or concerts after midnight... consider Las Vegas, for example.  Now you
can set the boundary to be 3 or 4am, so that when viewing the Day view for
Friday, the later events as late as 3am on Saturday morning will show up on the
Friday view.

Limitations: ONLY applies to Day and WeekByHour views, not to other views.
Therefore this could create some confusion among viewers who see a late night
event on Saturday night on the Day view, but finding that same event displayed
on Sunday on the month view. A fully consistent fix is for this situation is
difficult, and I'm unwilling to program it at this time.  I tried, and hence the
long delay between the 0.6.4 and 0.6.5 releases.  Instead I'm leaving it at this
for now."""

HELP_HOURSDISPLAY = u"""Code to tell the 'hoursdisplay' macro how to display the
hours in your calendar views. Currently two possibilities and they only affect
the left column display of hours: '12ampm' = 12 hour display, with am or
pm. Ex. 6 pm '24.00' = 24 hour display, with period. Ex. 20.00"""

HELP_USEHALFHOURS = u"""If checked, CalendarX will display half-hour increments
on the day and weekbyhour views instead of the default one-hour increments.
There remains NO capability of starting the day on the half-hour... the
dayViewStartHour and dayViewEndHour settings must be integer hour values. The
default value is blank (false), meaning Hourly periods will be used. There is a
modest performance penalty associated with this option, use at your
discretion."""

HELP_NUMMONTHSFORMULTIMONTHVIEW = u"""How many months to display in the month
view. Default value is 1, but may be extended up to 12 months.  Next buttons
move forward by one month, not by the number of months in the view.  Querying
time to generate several months at once may be excessive if many events are to
be shown."""

HELP_SHOWHEADERTITLEANDICONS = u"""If checked, CalendarX will display the
calendar title and description and email/print/favorites Action icons as it does
for other Plone content."""

HELP_SHOWHILIGHTFULLEVENT = u"""If checked, CalendarX will show the full extent
of Events on the calendar, even without rolling over with the mouse. Default is
a blue color, can be changed in CSS property sheet. NOTE! If you use this, you
might also want to disable the labelEventsOnlyAtStart property. Disabling
labelEventsOnlyAtStart means that the events in the Month view that span several
days will show labels for each of those days, instead of only on the first day
of the event."""

HELP_SHOWJUMPTODATEWIDGET = u"""If checked, a date-picking widget will show up
at the top and bottom of the calendar near the Next/Previous links. This widget
lets users pick a date and jump to it, instead of using multiple Next, Next,
Next click, or manually typing the date into the URL querystring."""

HELP_USENUMERICMONTHINJUMPTODATEWIDGET = u"""If checked, the Jump-To-Date widget
will show a numeric month value (ex. '2') instead of an abbreviation of the
month (ex. 'Feb'). These abbreviations are pulled from the python DateTime
module, not coded into CalendarX code, in the getMonthName.py script."""

HELP_SHOWPUBLICPRIVATELINK = u"""If checked, the *Public* vs *My Events* link
will be shown in the Subject Bar.  This link allows users to switch between
viewing all the published events, or ONLY their own private events. If your
calendar is mainly for viewing by anonymous users, you probably don't need
this. Default is OFF because this is a nice feature, but not a commonly chosen
one."""

HELP_USEMULTISUBJECTS = u"""If checked, the Subject category picker is a
checkbox-style form, allowing users to select multiple subjects for viewing. If
unchecked, it switches to (an older) single subject chooser that only allows one
Subject category at a time. Default is ON for this new-style Multi-Subject
chooser, because it is ever so much nicer."""

HELP_SHOWSUBJECTBAR = u"""If checked, the Subject bar is shown, and if
unchecked, it will disappear from view.  Default is ON.  Decomplicates the
calendar if you don't want to use Public/Private or Subject categories."""

HELP_USECALENDARHELP = u"""Check this attribute to show a View tab for 'Calendar
Help'.  This brings up a new view page that is intended for you to use for help
in case you have neophyte users who could use some calendar help.  I've added
some code that brings up one page of help for 'Members' and a different page of
help for 'Anonymous' users.  This could easily be extended to show different
help screens for other Roles.  See the 'help' view page template for more
information.  The help text is quite minimal, so feel free to expand it for your
users.  Feel free to send me a copy of your nice help files, too!"""

HELP_INCLUDEREVIEWSTATEVISIBLE = u"""Check this attribute to include events
where the review state is 'visible' as well as 'published'.  This is useful for
calendars where the only users are trusted users and going through the
publishing workflow only adds unnecessary complication.  In particular, this
could work well even on a site with many untrusted users.  In that case, create
a calendar for the trusted users that uses a repurposed Event with a new
portal_type name. Use the 'restrictToThisListOfTypes' attribute to make this new
calendar ONLY read this one type of Event.  Then use a getNotAddableTypes.py
script to restrict the use of this type of Event to your trusted users (as a
role, or a group, or whatever). See the HowTo on plone.org for use of
getNotAddableTypes."""

HELP_SHOWPENDINGLINK = u""" Check this attribute to show a link in the
subjectbar that, when clicked, tells the calendar to display events with
'pending' state as well as the other events (published, and visible if
includeReviewStateVisible has been selected).  The link is not a toggle; to get
out of the mode where the pending events are showing, simply click any other
link on the calendar.This link ONLY shows up for Calendar Managers.  Who is a
Calendar Manager? User status as a Calendar Manager is determined by the
isCalendarManager.py script.  It is easily customized, but as a default is set
to allow users with the 'Manager' role.  If this role is adequate for you, leave
this script as is.  An example is included in the script to show how to look up
group membership to determine Calendar Manager status."""

HELP_SHOWPRIVATEEVENTSTOGROUPMEMBERS = u""" Check this attribute to allow
PRIVATE events to show up to anyone with the Plone privilege of viewing your
PRIVATE events.  In short, what this does is allow you to give one of your
Groups or some other user a proxy ownership role for one of your
review_status=Private events.  That is enough to allow them to see it in
Plone. But this attribute must be TRUE (checked) if you want such events to show
up on a CalendarX instance."""

HELP_LISTOFREVIEWSTATESDISPLAYED = u"""List each review state (e.g.,
'published','external',etc.) that you wish to be displayed in your CalendarX.
These states will be appended to the list of any other review state choices
you've made using other attributes."""

HELP_SHOWONLYEVENTSINMONTH = u"""Check this attribute to restrict the Month view
to display events ONLY in the current calendar month, and NOT those events that
occur in the days before or after the month begins and ends (ie., if the month
view shows the 30th and 31st of the previous month on the calendar, events will
NOT be displayed for those dates."""

HELP_LABELEVENTSONLYATSTART = u"""Check this attribute to put labels on the
month view ONLY on the first day of an event that lasts multiple days.  Default
is SELECTED.  Unselect thisattribute if you'd like the event title and
datestring to appear on each calendar day that the event is on (ie., a four day
event will have the labelshow up on the calendar four times, on each of the four
days of the event). NOTE!  Disabling this (to show events on EVERY day) will
only work if the showHighlightFullEvent property is turned ON (selected).  It
would make no sense (to me) to have the event labeled, but not highlighted.  So
make sureyou use these together. No harm if you don't, but it won't behave the
way you might have expected. It pays to read the documentation."""

HELP_LISTOFSUBJECTS = u"""List of the subjects in your CalendarX, for use in
creating the macro that displays them on your calendar."""

HELP_LISTOFSUBJECTICONS = """The list consists of a lines attribute where each
line consists of a Subject and an icon ID, separated by a pipe ( | ) character.
For example: Work|event_work_icon.gif where Work is the subject. Your subject
names should (must!) match the actual subjects you use for your events, or this
method will not work well. Actually, it will just pull the default
event_icon.gif from the Plone skin if there is any problem finding a matching
subject name or icon ID. This property is handy for making your events more
visibly recognizable in your calendar page. The default icon size is 16x16
pixels, with some white (or clear) pixel space on the right and left sides. I
haven't tested it with larger icons, but keeping to a modest size might be a
good idea. Add your event icons into your /portal_skins/custom folder, or put
them directly into your calendar instance folder for (slightly) better
performance."""

HELP_LISTOFSUBJECTCSSCLASSES = """The list consists of a lines attribute where
each line consists of a Subject and a CSS class name, separated by a pipe ( | )
character. For example: US Holiday|event_usholiday where Work is the subject,
and event_usholiday is the CSS class name. Your subject names should (must!)
match the actual subjects you use for your events, or this method will not work
well. Actually, it will just pull the default event_published CSS class from the
Plone skin if there is any problem finding a matching subject name or icon ID.
This nicely allows you to apply styles like font color to your event listings
according to the Subject of the event. Put your custom styles into your
calendar.css stylesheet, or into a customized version of the ploneCustom.css
stylesheet if you prefer (the sample ones I've created for default use are found
in calendar.css). Additionally, if you want the Subjects in the Subject listing
at the top of the calendar to reflect these same CSS classes, you have to add
these too. Example ones (for Appointment, etc.) are in calendar.css for you to
customize. *** ONE MORE NOTE about these. Make sure in your
listOfSubjectCSSClasses and listOfSubjectIcons lines properties that you use the
actual SUBJECT name and not any Subject nicknames you might use for display (as
defined in the listOfSubjectTitles property in CX_props_calendar. Those labels
won't work here, only the actual subject will work. *** AND ONE MORE NOTE. The
following two properties (useEventTypeIcons and useEventTypeCSSClasses) take
precedence over useSubjectTypeIcons and useSubjectCSSClasses if, for unknown
reasons, BOTH have been selected. There's no real reason to select both... only
one can work at a time, and I chose to make the EventType ones take priority. Go
figure."""

HELP_LISTOFEVENTTYPEICONS = u"""The list consists of a lines attribute where
each line consists of an Event Type and an icon ID, separated by a pipe ( | )
character. For example: Event|event_icon.gif where Event is the portal_type."""

HELP_LISTOFEVENTTYPECSSCLASSES = u"""The list consists of a lines attribute
where each line consists of a Subject and a CSS class name, separated by a pipe
( | ) character. For example: AT Event|atevent_class where AT Event is the
portal_type, and atevent_class is the CSS class name."""

HELP_USESUBCALENDARSUBJECTMENU = u"""For MAIN Calendars: Check this property to
signal that (1) there are subcalendars below and (2) hence, use the special
SubCalendar Menu for the Subject Links that allows you to both (either) filter
on the subcalendars as well as click on the Subject (subcalendar name) to drill
down and view that subcalendar alone."""

HELP_LISTOFSUBCALENDARS = u"""For MAIN Calendars: This is a list (one per line)
of names (or nicknames) of the subcalendars. The menu choices uses this list for
display of links to the subcalendars. USE THE SAME ORDER AS IN THE List of
SubCalendar IDs ABOVE."""
