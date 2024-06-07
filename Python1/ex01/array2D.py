import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    '''
    Slice a 2D array
        Parameters:
            family: list
                A list of lists
            start: int
                The index of the first element to include in the slice
            end: int
                The index of the last element to include in the slice
        Returns:
            list
                A slice of the 2D array
    '''
    try:
        arr = np.array(family)[start:end]
        print("My shape is : ", np.array(family).shape)
    except IndexError:
        print("Index out of range")
        return list()
    except ValueError:
        print("The lists are not the same size")
        return list()
    except Exception as e:
        print("An error occurred: ", e)
        return list()
    print("My new shape is : ", arr.shape)
    return arr.tolist()
