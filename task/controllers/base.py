# -*- coding: utf-8 -*-
"""
    task.controllers.base
    ~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013 by Abhinav Singh.
    :license: BSD, see LICENSE for more details.
"""
from functools import wraps


def base(ctrl):
    @wraps(ctrl)
    def wrapper(t, *args, **kwargs):
        try:
            ctrl(t, *args, **kwargs)
        except KeyboardInterrupt, _: # pragma: no cover
            pass
        except: # pragma: no cover
            raise
        finally:
            t.stop()

        if t.exception:
            raise t.exception
        return t.result
    return wrapper
