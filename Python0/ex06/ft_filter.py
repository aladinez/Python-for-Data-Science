
def ft_filter(func, iterable):
    """
ft_filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    """
    try:
        iter(iterable)
    except TypeError:
        print("TypeError: 'function' object is not iterable")
        return
    if func is None:
        return [n for n in iterable]

    return [n for n in iterable if func(n)]
