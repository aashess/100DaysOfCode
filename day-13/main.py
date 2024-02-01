# import random

# list = [1,2,3,4,5]
# choic = random.randint(1,4)
# print(list[choic])

def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)

mutate([1,2,3,4,5])