
import collections

class def_dict(collections.defaultdict):
    """ Create a dict that returns a default value if queried with a missing key

    
    >>> z=def_dict((-99,-99))
    >>> z['foo']
    (-99, -99)
    >>> z['foo']=99
    >>> z['foo']
    99
    >>> z['bar']=123
    >>> sorted(z.keys())
    ['bar', 'foo']

    """


    def __missing__(self, key):
        return self.__mv__
    def __init__(self, missingvalue):
        super(def_dict, self).__init__()
        self.__mv__ = missingvalue

if __name__ == "__main__":
    import doctest
    doctest.testmod()
