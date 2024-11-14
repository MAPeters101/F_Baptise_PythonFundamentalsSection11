
# a = 1
# b = 0
# result = a / b
# print(result)

ex = ValueError('Name must be at least 5 characters long.')
print(type(ex))
print(ex)
print(repr(ex))
print(str(ex))

#raise ex

# name = input("Enter name (5 character min): ")
# if len(name) < 5:
#     raise ValueError(f'{name} is not 5 characters or more...')
# print(f'Hello {name}!')

print()
print(issubclass(KeyError, LookupError))
print(issubclass(KeyError, Exception))
print(issubclass(IndexError, LookupError))
print()

ex = KeyError('some message')
print(type(ex))
print(isinstance(ex, KeyError))
print(isinstance(ex, LookupError))
print(isinstance(ex, Exception))
print(isinstance(ex, IndexError))




