def find_string_power_set(chars: str) -> list[str]:
    """
    Find every possible subset of all the characters in the string and return them in a list.

    Sets are unordered collections of unique items.  
        {'a', 'b', 'c'} is a set 
        {'a', 'a', 'b'} is not a set because there are duplicate 'a's
    
    A subset is a set that has less items than another set but all of its items are apart of that other set. 
        {'a'} is a subset of {'a', 'b', 'c'}
        {'a', 'd'} is not a subset of {'a', 'b', 'c'} because the second set does not have a 'd'


    For example, if given the string "ABC", find_string_power_set("ABC") shoud return:

        ["ABC", "AB", "AC", "A", "BC", "B", "C"]
    
    If the string argument chars has duplicate characters, make sure the returned list does not contain "sets" with duplicates
    """

    if chars == '':
        return ['']
    
    power_set = []
    head, rest = chars[0], chars[1:]

    rest_powersets = find_string_power_set(rest)

    for rest_set in rest_powersets:
        power_set.append(head + rest_set)

    power_set = power_set + rest_powersets
    return power_set