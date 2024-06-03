from collections.abc import Iterable

def flatten(*args):
    """
    Take any number of arguments and 'flatten' them into a single list so they exist within the same level of arguments. Only flatten collections and not all iterables like strings. 

        flatten(5, 'string') -> [5, 'string']
        flatten([1, 2, 3], [4, [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    
    """
    # base case - can't be broken down anymore
    results = []
    for arg in args:
        if isinstance(arg, Iterable) and isinstance(arg, str) == False:
            for i in arg:
                results.extend(flatten(i))
        else:
            results.append(arg)
    return results
