# -*- coding: utf-8 -*-
# python3

data_user = ('Candido', 'email@email.com', '(11) 777777777', '(11) 555555555', '(11) 999999999')

name, email, *phone = data_user

print(name)
print(email)
print(phone)

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]

print(trailing)
print(current)