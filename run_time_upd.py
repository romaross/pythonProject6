import datetime
import datetime as dt
from random import randint as rnd
import sys


def running_time(func):
    ret_val = None

    def wrapper(*args, **kwargs):
        nonlocal ret_val
        start = dt.datetime.now()
        ret_val = \
            func(*args, **kwargs)
        finish = dt.datetime.now()
        run_time = finish - start
        if run_time >= datetime.timedelta(microseconds=100):
            print('Оборачиваемая функция  {} время выполнения {}'.format(func.__name__, run_time), file=sys.stderr)
        return ret_val
    return wrapper


@running_time
def main_func():
    """ Test function """
    print(' A long long circle..')
    for _ in range(rnd(1e7, 1e8)):
        continue
    return ' Heating finishing.'


print(' main result ', main_func())
