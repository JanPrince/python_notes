def increment_string(strng):
    """
    :parameter = a string
    :returns :
    If the string already ends with a number, the number should be incremented by 1.
    If the string does not end with a number. the number 1 should be appended to the new string.

    """
    nums = []
    chars = []
    for i in strng:
        if i.isdigit():
            nums.append(i)
        else:
            chars.append(i)


    num_str = str("".join(nums))
    if len(nums) == 0:
        num_str = '0'
    num_int = int(num_str)

    num_incre = num_int + 1
    chars_str = "".join(chars)

    strng = chars_str + str(num_incre)
    return strng

name = "hello"
name1 = "hello45"
name9 = 'prince9999'
print(increment_string(name1))
print(increment_string(name9))
print(increment_string(name))

"""
NB: isdigit(), isnumeric() functions are used to verify if a string contains only numbers or not

        name = "prince112"
        isdigit(name)     produces false
"""