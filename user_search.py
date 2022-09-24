# поиск пользователей
def search (user_list):
	request = input('Кого мы ищем? \n ')
	t = True
	for i in user_list:
		if i['LastName'] == request or i['Name'] == request or i['Number'] == request: 
			t = False
			return print(*i.values())
	if t:
		return print('Нет такого usera')
