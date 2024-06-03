my_dict = {'Igor': 1995, 'Rustam': 1996, 'Nastya': 1997}
print(my_dict)
print(my_dict['Nastya'])
my_dict['Alex'] = 1999
print(my_dict['Alex'])
my_dict.update({'Anna': 1993, 'Vladimir': 1998})
print(my_dict)
del my_dict['Anna']
print(my_dict.get('Anna'))
print(my_dict)
set_ = {False, 1, 2, 2, 'Volna', False, 'Volna'}
print(set_)
set_.add('Eagle')
set_.add(945.56)
set_.discard(False)
print(set_)


