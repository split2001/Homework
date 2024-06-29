calls = 0
def count_calls():
    global calls
    calls +=1
    return calls
def string_info(string):
    count_calls()
    tuple_ = len(string), string.upper(), string.lower()
    return tuple_

def is_contains(string, list_to_search):
    count_calls()
    if string.lower() not in list(map(str.lower,list_to_search)):
        return False
    else:
        return True

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
