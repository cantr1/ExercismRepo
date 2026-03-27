#TODO: define the 'EXPECTED_BAKE_TIME' constant below.
""" Constant for baking time
"""
EXPECTED_BAKE_TIME=40


#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(time_elapsed):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - time_elapsed


#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider defining a 'PREPARATION_TIME' constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations.
def preparation_time_in_minutes(number_of_layers):
    """ Return the prep time
        :params number_of_layers = the number of layers
    """
    return 2 * number_of_layers
    


#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """ Return the elapsed time
        :params number_of_layers = the number of layers
        :params elapsed_bake_time = the time since process started
    """
    return ((number_of_layers * 2) + elapsed_bake_time)
    


# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
