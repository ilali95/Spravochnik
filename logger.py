from datetime import datetime as dt

def data_recording(data):
	time = dt.now().strftime('%H:%M')
	with open('log.csv', 'a') as file:
		file.write('{};recording;{}\n'
					.format(time, data))