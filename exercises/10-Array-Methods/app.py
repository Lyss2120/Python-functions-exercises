names = ['John', 'Kenny', 'Tom', 'Bob', 'Dilan']
## CREATE YOUR FUNCTION HERE
def sort_names(list):
    list2 = sorted(list)
    return list2

print(sort_names(names))

# The sort() method sorts the list ascending by default.
# You can also make a function to decide the sorting criteria(s).