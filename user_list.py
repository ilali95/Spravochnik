# Получить список(пользователей) разбиты на словари внутри
from urllib import request

def get_list(rad):
	f = open('data.txt', 'r', encoding="utf-8")
	num = f.readlines()
	user_list = []
	for i in num:
		raw_test = i.split()
		user_data = { 'LastName': raw_test[0],'Name': raw_test[1], 'Number': raw_test[2]}
		user_list.append(user_data)
	f.close()
	return user_list