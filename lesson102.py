
try:
    1/0
except ZeroDivisionError as ex:
    print(f'Exception occured: {type(ex)}, {ex}')
print('Code continues running here...')
print()


l = [1, 2, 3, 4, 5]
while len(l) > 0:
    print(l.pop())
print('all done')
print()


# l = [1, 2, 3, 4, 5]
# while True:
#     print(l.pop())
# print('all done')
# print()


l = [1, 2, 3, 4, 5]
try:
    while True:
        print(l.pop())
except IndexError:
    # index error means list is now empty - expected behavior.
    print('All done - all elements have been popped.')
print('Code resumes here...')
print()


l = [1, 2, 3, 4, 5]
try:
    while True:
        print(l.pop())
except Exception:
    print('Something unexpected happened.')
print('Code resumes here...')
print('='*80)


l = (1, 2, 3, 4, 5)
try:
    while True:
        print(l.pop())
except Exception:
    print('All done - all elements have been popped.')
print('Code resumes here...')
print(l)
print()


# l = (1, 2, 3, 4, 5)
# try:
#     while True:
#         print(l.pop())
# except IndexError:
#     print('All done - all elements have been popped.')
# print('Code resumes here...')
# print(l)
# print()

print('='*80)
#print(10 + 'abc')
#print(10 + None)
print(10)
print()

data = [10, 20, 10, 10, 5, 10]
sum_data = 0
count_data = 0
for element in data:
    sum_data += element
    count_data += 1
average = sum_data / count_data
print(f'average = {average}')
print()


# data = []
# sum_data = 0
# count_data = 0
# for element in data:
#     sum_data += element
#     count_data += 1
# average = sum_data / count_data
# print(f'average = {average}')
# print()


data = []
if len(data) == 0:
    average = 0
else:
    sum_data = 0
    count_data = 0
    for element in data:
        sum_data += element
        count_data += 1
    average = sum_data / count_data
print(f'average = {average}')
print()


data = [10, 20, 'abc']
sum_data = 0
count_data = 0
try:
    for element in data:
        sum_data += element
        count_data += 1
    average = sum_data / count_data
except ZeroDivisionError:
    average = 0
except TypeError:
    average = 0
print(f'average = {average}')
print()



