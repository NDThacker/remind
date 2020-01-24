import argparse
import datetime
import pprint
import time
from scripts import pickling
from scripts import filterSearch

eventList = []

class Event:
	def __init__(self, title, eDate, desc):
		self.title = title
		self.eDate = eDate
		self.desc = desc

def addEvent(eventList):
	''' add an event '''

	eTitle = input('Enter Event Title')
	eDate = input('Enter Event Date and Time')
	eDesc = input('Enter Event Description')

	event = Event(eTitle, time.strptime(eDate, "%d %b %Y, %H:%M"), eDesc)
	eventList.append(event)
	pprint('Event added Successfully')

def viewAll(events):
	''' prints all events '''

	for event in events:
		viewOne(event)

def viewOne(event):
	''' prints a single event '''

	print('Title: {}\nDate & Time: {}\n Description:\
		 {}\n'.format(event.title, time.asctime(event.eDate), event.eDesc))

parser = argparse.ArgumentParser(description = 'Event Reminder Utility')

# parser.add_argument('--add', action = 'store_true', help = 'flag to add an event reminder')
parser.add_argument('--today', action = 'store_true', help = 'flag to display all events for today')
parser.add_argument('--delete', action = 'store_true', help = 'flag to delete an event')
parser.add_argument('--for-date', default = datetime.date.today(), \
help = 'events for a specific given date (format: dd abbreviated-month yyyy, hh:mm) e.g 30 Nov 2020, 20:35')
parser.add_argument('--range', default = False, help = \
'two dates separated by space as range to extract events from (format: MM/DD/YYYY)')
parser.add_argument('--view-all', action = 'store_true', help = 'display all the events from today')

args = vars(parser.parse_args())


if args.get('today'):
	events = filterSearch.extractForToday()
	viewAll(events)
elif args.get('view-all'):
	viewAll(eventList)
elif args.get('delete'):
	pass
elif args.get('for-date'):
	events = filterSearch.extractForSpecificDate(args.get('for-date'), eventList)
	viewAll(events)
elif args.get('range'):
	datesStr = args.get('range')
	dateL = datesStr.split()
	date1 = dateL[0]
	date2 = dateL[1]
	events = filterSearch.extractForRange(date1, date2, eventList)
	viewAll(events)
else:
	addEvent(eventList)

