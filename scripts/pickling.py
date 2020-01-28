#!/usr/bin/env python
import pickle


def loadEvents():
	try:
		dataFile = open('../data/eventsData.pkl', 'rb')
	except:
		return []
	eventList = pickle.load(dataFile)
	dataFile.close()
	return eventList


def saveEvents(eventList):
	dataFile = open('../data/eventsData.pkl', 'wb')
	pickle.dump(eventList, dataFile)
	dataFile.close()
	return
	