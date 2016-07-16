import time

class Helper:
	def generateFileName(self, prefix, name): 
		timestamp = time.strftime("%m:%d:%y:%H:%M:%S")
		fileName = "{}_{}_{}".format( prefix, name, timestamp )
                return fileName

