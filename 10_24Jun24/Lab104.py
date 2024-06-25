numbers = [1,2,3,4,5,6,7,8,9,10]

def even_giver(n):
    return n % 2 ==0

# new_filtered_list = list(filter(even_giver, numbers))
new_filtered_list = list(filter(lambda x : x % 2 == 0, numbers))

print(list(new_filtered_list))

