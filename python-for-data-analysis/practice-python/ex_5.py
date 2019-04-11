

import random

def rand_list_factory(rand_list_len):
    rand_list = []
    for i in range(rand_list_len):
        rand_list.append(random.randint(1,101))
    return(rand_list)



rand_list_len_1 = random.randint(5,101)
rand_list_len_2 = random.randint(5,101)

rand_list_1 = rand_list_factory(rand_list_len_1)
rand_list_2 = rand_list_factory(rand_list_len_2)

''' TESTING LISTS
rand_list_1 = [1,2,3,4,5,6,7,8,9]
rand_list_2 = [10,9,5,23,1,55]
'''

same_list = []
diff_list = []

same_list = [num for num in rand_list_1 if num in rand_list_2]

print('List one: {} '.format(rand_list_1))
print('List two: {} '.format(rand_list_2))
print(same_list)
