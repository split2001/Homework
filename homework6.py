immutable_var = (1, 'lesson', False)
print(type(immutable_var))
print(immutable_var)
mutable_list = ['shorts', 'T-short', 'pants', 'swimsuit', 'scarf']
print(mutable_list)
mutable_list[0] = 'tie'
mutable_list[4] = 'hat'
print(mutable_list)
mutable_list.append('bagpack')
mutable_list.remove('pants')
print(mutable_list)
immutable_var[1] = 'homework'
print(immutable_var)#Кортежи являются неизменяемыми коллекциями
