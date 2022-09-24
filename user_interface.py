from urllib import request
import user_list as ul
import logger as log

def user_view(lst):
	data = ul.get_list(lst)
	log.data_recording(data)
	return data