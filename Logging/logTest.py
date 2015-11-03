import logging

#1 DEBUG - detailed
#2 INFO - confirmation that things are running correctly
#3 WARNING - (default), something unexpected
#4 ERROR - some function failed
#5 CRITICAL - something failed critically and must be closed

# Use .log file which in programming is a file that records events
# use logger.setlevel('string') to dynamically set log level. 


# don't include the line below if you want to log in console. 
logging.basicConfig(filename='ErrorLog.log', setlevel='DEBUG') #DEBUG is threshold


def main():
	try:
		logging.debug('Entered main() function for log')
		mathFail = 1/0
		if 1 > 2 : 
			logging.debug('Entered main if statement')
			print 1
		else:
			logging.info('Entered else function')
			print 0


	except Exception, e:
		logging.critical(str(e))  #critical in this case is a label, but can be any, shows up as "CRITICAL"

if __name__ == '__main__':
	main()