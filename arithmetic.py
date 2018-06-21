"""Math functions for calculator."""
import functools
def reduce(function, lst):
    if len(lst) == 1:
        return lst[0]
    elif len(lst) == 0:
        return "list is empty"
    else:
        answer = lst[0]
        for num in lst[1:]:
            answer = function(answer, num)

        return answer





def add(nums):
    """Return the sum of the two inputs."""

    return sum(nums)


def subtract(nums):
    """Return the second number subtracted from the first."""

    # answer = nums[0]
    # for num in nums[1:]:
    #     answer -= num

    # return answer

    return reduce(lambda x, y: x-y, nums)


def multiply(nums):
    """Multiply the two inputs together."""

    # answer = nums[0]
    # for num in nums[1:]:
    #     answer *= num

    # return answer
    return functools.reduce(lambda x, y: x*y, nums)

def divide(nums):
    """Divide the first input by the second and return the result."""

    # answer = nums[0]
    # for num in nums[1:]:
    #     answer /= num

    # return answer
    return functools.reduce(lambda x, y: x/y, nums)


def square(nums):
    """Return the square of the input."""

    return nums[0] ** 2


def cube(nums):
    """Return the cube of the input."""

    return nums[0] ** 3


def power(nums):
    """Raise num1 to the power of num2 and return the value."""

    return nums[0] ** nums[1]


def mod(nums):
    """Return the remainder of num1 / num2."""

    # answer = nums[0]
    # for num in nums[1:]:
    #     answer %= num

    # return answer
    return functools.reduce(lambda x, y: x%y, nums)


def add_mult(nums):
    """Return the total from adding num1 and num2 and multipling sum by num3"""

    return (nums[0] + nums[1]) * nums[2]


def add_cubes(nums):
    """Return the sum of the cubes of num1 and num2"""

    return cube(nums[0]) + cube(nums[1])

    