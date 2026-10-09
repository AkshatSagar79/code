def GetItemsWithMinFrequency(my_list, k):

    result = []

    for x in my_list:
        frequency = my_list.count(x)

        if frequency >= k and x not in result:
            result.append(x)

    return result

my_list = [3,5,3,2,2,2,3,6,7,7]
print(GetItemsWithMinFrequency(my_list,1))
print(GetItemsWithMinFrequency(my_list,2))
print(GetItemsWithMinFrequency(my_list,3))
print(GetItemsWithMinFrequency(my_list,4))