def calculate_structure_sum(*data_structure):
  result_sum = 0
  for i in data_structure:
    if isinstance(i, dict):
      last_dict = list(i.items())
      result_sum += calculate_structure_sum(last_dict)
    elif isinstance(i, str):
      result_sum += len(i)
    elif isinstance(i, int):
      result_sum += i
    else:
      result_sum += calculate_structure_sum(*i)
  return result_sum


data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}),
                  "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
result = calculate_structure_sum(data_structure)
print(result)
