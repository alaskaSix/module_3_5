def get_multiplied_digits(numder):
    str_number = str(numder)
    firs = int(str_number[0])
    if len(str_number) > 1:
        return firs * get_multiplied_digits(int(str_number[1:]))
    else:
        return firs


# (firs * get_multiplied_digits(int(str_number[1:])))
result = get_multiplied_digits(40203)
print(result)