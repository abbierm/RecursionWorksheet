# Returns a list of lists containing the different orders the items could be assuming the items can be repeated as many times. 
# Function takes length of the desired output as an argument, if none is given, the length will be set to be the length of the list. 
# Items can be repeated 0 to the length times. Not all items need to be in the output. 


def list_perms(array: list, length=None, current=None):
    if length is None:
        length = len(array)
    if current is None:
        current = []
    
    # Base Case
    if length == 0:
        return [current]

    results = []
    for item in array:
        new = current + [item]
        results.extend(list_perms(array, length - 1, new))

    return results
