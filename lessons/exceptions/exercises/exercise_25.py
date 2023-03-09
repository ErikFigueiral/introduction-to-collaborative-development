def weird_number(arg: int) ->float:
    """Function that accepts a float representation that returns it cube if it
    is possible,otherwise it will be considered 0.Later,@arg will be increased.

    This function will raise a exception if the @arg isn't a float,int or string.
    In any other case will do the description above.
    Args:
        arg (int,float,string):
    Returns:
        float:Result of the operation with @arg.
    Raise:
        TypeError:If @arg is a not desired data type.
    """
    if not isinstance(arg,(int,float,str)):
        raise TypeError("this function only accepts integers,"
                        "floats and strings.")
    try:
        arg : float = float(arg)
        arg : float = arg ** 3
    except ValueError:
        arg : float = float(0)
    finally:
        arg : float = arg + 1
    return arg
