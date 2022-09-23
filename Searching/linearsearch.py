def linear_search(list, target):
    for i,j in enumerate(list):
        if j == target:
            return i
    return None


print(linear_search([1,2,3,4,5,6,7,8,9,10], 5))