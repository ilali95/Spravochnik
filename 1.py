# Разделим сервис на этапы:
# Как можно вводить данные?
# ‘Фамилия Имя Номер’
# Как их обрабатывать? Где хранить?
# user = {‘Name’:’’, ‘Last Name’:’’, ‘number’:’’ }
# user_list = [user1,user2,user3……]
# Как запрашивать и получать данные?
# Какие функции можно для этого создать? 
# Как вынести функции в модули?
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


# Как запрашивать и получать данные?


def search (user_list):
	request = input('Кого мы ищем? \n ')
	t = True
	for i in user_list:
		if i['LastName'] == request or i['Name'] == request or i['Number'] == request: 
			t = False
			return print(*i.values())
	if t:
		return print('Нет такого usera')


r = 'data.txt'
user_list = get_list(r)
search(user_list)