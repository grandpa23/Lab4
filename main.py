import traceback
import re

def exception(trace):
    file_name = "main.py"
    line = re.search("line \d+", trace.split("\n")[1]).group(0)[5:]
    exception = trace.split("\n")[-2].strip()
    print("Ошибка в строке", line,  tree[file_name + ' ' + line][exception][hash(trace)])
if __name__ == '__main__':
    errors = [
            ["main.py 44", "KeyError",
            "Traceback (most recent call last):\n  File \"main.py\", line 44, in <module>\n    raise KeyError()\nKeyError\n",
            "Ключ не найден"],
            
            ["main.py 48", "TimeoutError",
            "Traceback (most recent call last):\n  File \"main.py\", line 48, in <module>\n    raise TimeoutError()\nTimeoutError\n",
            "Время ожидания истекло"],
            
            ["main.py 52", "TypeError",
            "Traceback (most recent call last):\n  File \"main.py\", line 52, in <module>\n    raise TypeError()\nTypeError\n",
            "Неверный тип данных"],
            
            ["main.py 56", "IndexError",
            "Traceback (most recent call last):\n  File \"main.py\", line 56, in <module>\n    raise IndexError()\nIndexError\n",
            "Индекс вышел за пределы последовательности"],
            
            ["main.py 60", "ImportError",
            "Traceback (most recent call last):\n  File \"main.py\", line 60, in <module>\n    raise ImportError()\nImportError\n",
            "Ошибка иморта библиотеки, попробуйте pip"],
            
            ["main.py 64", "ZeroDivisionError",
            "Traceback (most recent call last):\n  File \"main.py\", line 64, in <module>\n    raise ZeroDivisionError()\nZeroDivisionError\n",
            "Деление на ноль"],
                        
            ["main.py 68", "MemoryError",
            "Traceback (most recent call last):\n  File \"main.py\", line 68, in <module>\n    raise MemoryError()\nMemoryError\n",
            "Операции не хватает памяти для выполнения"]
            ]
    tree = {}
    for i in errors:
        tree[i[0]] = {i[1]:{hash(i[2]): i[3]}}

    try:
        raise KeyError()
    except:
        exception(traceback.format_exc())
    try:
        raise TimeoutError()
    except:
        exception(traceback.format_exc())
    try:
        raise TypeError()
    except:
        exception(traceback.format_exc())
    try:
        raise IndexError()
    except:
        exception(traceback.format_exc())
    try:
        raise ImportError()
    except:
        exception(traceback.format_exc())
    try:
        raise ZeroDivisionError()
    except:
        exception(traceback.format_exc())
    try:
        raise MemoryError()
    except:
        exception(traceback.format_exc())
