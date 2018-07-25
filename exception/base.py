"""Exception

Sytnax:
    IndentationError
    SytnaxError
    NameError

DataAccess:
    IndexError  # [1, 2][3]
    ValueError  # int('a')
    TypeError   # 2 + "a"
    KeyError    # {'a': 1}['b']

Import:
    ModuleNotFoundError # import a python3
    ImportError         # import a python2
"""
import traceback

def add(x, y):
    result = None

    try:
        result = int(x) + int(y)
    # except (ValueError, TypeError):
    #     print('error')
    except Exception as err:
        traceback.print_exc()
        print(str(err))
    # except ValueError:
    #     print('value error')
    # except TypeError:
    #     print('type error')
    else:
        print('everything ok')
    finally:
        print('clear up')

    return result

add(1, 2)

add(1, 'str')

add(1, [1,2])

issubclass(TypeError, Exception)

raise ValueError('hello')
