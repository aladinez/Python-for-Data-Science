

def count_in_list(lst: list, element: str):
    '''
    Count the number of times an element appears in a list.
    '''

    try:
        lst = list(lst)
        count = lst.count(element)
    except TypeError:
        return 0
    return count
