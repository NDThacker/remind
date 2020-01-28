#!/usr/bin/env python

import sys,os
# sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
import argparse
import datetime
import pprint
import time
from pickling import loadEvents, saveEvents
from filterSearch import extractForRange, extractForSpecificDate, extractForToday
eventList = []


def loadDataDump():
	eventList.extend(loadEvents())
	# print(*eventList)

def saveDataDump():
	saveEvents(eventList)


#Event class
class Event:
	def __init__(self, title, eDate, desc):
		self.title = title
		self.eDate = eDate
		self.eDesc = desc
	def __str__(self):
		return('Title: {}\nDate & Time: {}\nDescription:{}\n'\
			.format(self.title, time.asctime(self.eDate), self.eDesc))

def addEvent():
	''' add an event '''
	eTitle = input('Enter Event Title: ')
	eDate = input('Enter Event Date and Time, format example 30 Nov 2020, 23:10: ')
	eDesc = input('Enter Event Description: ')

	event = Event(eTitle, time.strptime(eDate, "%d %b %Y, %H:%M"), eDesc)
	eventList.append(event)
	print('Event added Successfully')

def viewAll(events):
	''' prints all events '''
	for event in events:
		viewOne(event)

def viewOne(event):
	''' prints a single event '''
	print('Title: {}\nDate & Time: {}\nDescription: {}\n'\
		.format(event.title, time.asctime(event.eDate), event.eDesc))
#---------------------------------Set up---------------------------------------
loadDataDump()
parser = argparse.ArgumentParser(description = 'Event Reminder Utility')

# parser.add_argument('--add', action = 'store_true', help = 'flag to add an event reminder')
parser.add_argument('--today', action = 'store_true', help = 'flag to display all events for today')
parser.add_argument('--delete', action = 'store_true', help = 'flag to delete an event')
parser.add_argument('--for-date', default = datetime.date.today(), \
help = 'events for a specific given date (format: dd-mm-yyyy)')
parser.add_argument('--range', default = False, help = \
'two dates separated by space as range to extract events from (format: MM/DD/YYYY)')
parser.add_argument('--view-all', action = 'store_true', help = 'display all the events from today')

args = vars(parser.parse_args())

print(args)
if args.get('today'):
	events = extractForToday(eventList)
	viewAll(events)
elif args.get('view_all'):
	viewAll(eventList)
elif args.get('delete'):
	pass
elif args.get('for_date'):
	events = extractForSpecificDate(args.get('for_date'), eventList)
	viewAll(events)
elif args.get('range'):
	datesStr = args.get('range')
	dateL = datesStr.split()
	date1 = dateL[0]
	date2 = dateL[1]
	events = extractForRange(date1, date2, eventList)
	viewAll(events)
else:
	addEvent()
	saveDataDump()


