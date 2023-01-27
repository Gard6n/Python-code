
def linearsearch(list, target):
    
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def varift(index):
    if index is not None:
        print('Target found at index: ', index)
    else:
        print('Target not found in list')
    
num = [1,2,3,4,5,6,7,8,9,10]

done = linearsearch(num,10)

varift(done)