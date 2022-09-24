# Разделим сервис на этапы:
# Как можно вводить данные?
# ‘Фамилия Имя Номер’
# Как их обрабатывать? Где хранить?
# user = {‘Name’:’’, ‘Last Name’:’’, ‘number’:’’ }
# user_list = [user1,user2,user3……]
# Как запрашивать и получать данные?
# Какие функции можно для этого создать? 
# Как вынести функции в модули?

import controller as ct

r = 'data.txt'
user_list = ct.get_list(r)
ct.user_view(user_list)
ct.search(user_list)