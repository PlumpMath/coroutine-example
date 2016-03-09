from functools import wraps

def coroutine(generator):
    """Make sure we don't have to call `next` on a just-started coroutine."""

    @wraps(generator)
    def new_cr(*args, **kwargs):
        g = generator(*args, **kwargs)
        next(g)
        return g

    return new_cr
