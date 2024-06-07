import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    '''
    This function calculates the BMI of a person.
    param height: A list of heights of people.
    param weight: A list of weights of people.
    return: A list of BMI of people.
    '''
    return np.divide(weight, np.square(height)).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''
    This function checks if the BMI of a person is less than limit.
    param bmi: A list of BMI of people.
    param limit: A limit to check against the BMI.
    return: A list of boolean values of BMI less than limit.
    '''
    return np.greater(bmi, limit).tolist()
