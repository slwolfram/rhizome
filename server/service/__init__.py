import functools
from ..repository import get_db


def transaction(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        db = get_db()
        kwargs['db'] = db
        result = func(*args, **kwargs)
        db.commit()
        db.close()
        return result
    return wrapper
