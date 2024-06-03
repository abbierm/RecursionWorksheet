

def flatten(*args):
    """
    Take any number of arguments and 'flatten' them into a single list so they exist within the same level of arguments. Only flatten collections and not all iterables like strings. 

        flatten(5, 'string') -> [5, 'string']
        flatten([1, 2, 3], [4, [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    
    """
    # base case - can't be broken down anymore
    results = []
    for arg in args:
        try:
            if len(arg) == 1 or isinstance(arg, str):
                results.append(arg)
            else:
                for x in arg:
                    results.extend(flatten(x))
        except TypeError:
            results.append(arg)
    return results