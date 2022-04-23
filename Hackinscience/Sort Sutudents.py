def sort_a_list(a_list):
    return sorted(a_list,reverse=True)

def sort_by_mark(my_class):
    return sorted(my_class,key=lambda my_class:my_class[0],reverse=True)

def sort_by_name(my_class):
    return sorted(my_class,key=lambda my_class:my_class[1])

print(sort_a_list([3, 2, 1]))   #should print [1, 2, 3]
my_class = [(25, "Shannon"), (50, "Alan"), (75, "Aza")]
print(sort_by_mark(my_class))
print(sort_by_name(my_class))