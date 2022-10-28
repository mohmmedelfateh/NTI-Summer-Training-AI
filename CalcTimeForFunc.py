def decorator_timer(some_function):
    from time import time

    def wrapper(*args, **kwargs):
        t1 = time()
        res = some_function(*args, **kwargs)
        end = time() - t1
        return res, end

    return wrapper


@decorator_timer
def my_pow(a, b):
    res = a ** b
    return res


result, exec_time = my_pow(99999, 99999)
print(exec_time)
print(result)
