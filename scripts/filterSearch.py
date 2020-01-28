#!/usr/bin/env python

import time
import datetime
import calendar


def extractForToday(eventList):
	today_struct = time.strptime(datetime.date.today().strftime("%Y-%m-%d"), "%Y-%m-%d")
	resList = filter(lambda event : 
		(event.eDate.tm_year == today_struct.tm_year and \
			event.eDate.tm_mon == today_struct.tm_mon and event.eDate.tm_mday == today_struct.tm_mday),
		eventList)
	return resList


def extractForSpecificDate(dateStr, eventList):
	date_struct = time.strptime(dateStr, "%d-%m-%Y")
	resList = filter(lambda event : 
		(event.eDate.tm_year == date_struct.tm_year and \
			event.eDate.tm_mon == date_struct.tm_mon and event.eDate.tm_mday == date_struct.tm_mday),
		eventList)
	return resList

def extractForRange(dateStr1, dateStr2, eventList):
	date1_struct = time.strptime(dateStr1, "%d-%m-%Y")
	date2_struct = time.strptime(dateStr2, "%d-%m-%Y")
	resList = filter(lambda event : 
		(event.eDate.tm_year >= date1_struct.tm_year and \
			event.eDate.tm_mon >= date1_struct.tm_mon and \
			event.eDate.tm_mday >= date1_struct.tm_mday and event.eDate.tm_year <= date2_struct.tm_year\
			and event.eDate.tm_mon <= date2_struct.tm_mon and \
			event.eDate.tm_mday < date2_struct.tm_mday),
		eventList)
	return resList
