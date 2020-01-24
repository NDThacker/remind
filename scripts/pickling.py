import pickle


def loadEvents():
	dataFile = open('../data/eventsData', 'rb')
	eventList = pickle.load(dataFile)
	dataFile.close()
	return eventList


def saveEvents(eventList):
	dataFile = open('../data/eventsData', 'wb')
	pickle.dump(eventList, dataFile)
	return
	