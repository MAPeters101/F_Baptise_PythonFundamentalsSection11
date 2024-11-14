
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



