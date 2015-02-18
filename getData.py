import time, datetime
import rtpi

# examle inputs:
# table = 'r' # r for realtime bus information, t for timetable information
# stop = '262'
# route = '16' #optional
# fo = 'j' # format = xml/json?

# This UI is designed for testing 
while True:

	# Get table type
	print "What Dublinbus information you want to retrieve? "
	table = raw_input("""USAGE:\n'r' for realtime bus information\n't' for timetable informationn\n'i' for route informationn\n'l' for route list informationn\n'q' to quit: """)
	# Check if quit
	if table in ('q', 'Q'):
		print 'QUIT'
		exit()
	# Check if realtime info or timetable info
	if table not in ('r', 't', 'R', 'T', 'i', 'I', 'l', 'L'):
		print """Please enter in 'r', 't', 'i' or 'l'."""
		continue	
	table = table 

	# Get bus stop no.
	stop = raw_input('''What bus stop no. you're looking for: ''')
	# Check if a number
	stop = stop
	
	# Get bus route no.
	route = raw_input('''What bus route you're looking for: ''')
	# Check if a number
	route = route


	
	# Print results
	print('BEFORE: %s' % time.ctime())
	rtpi.ppdata(table, str(stop), str(route), 'json')
	print('AFTER: %s\n' % time.ctime())

