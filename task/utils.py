# -*- coding: utf-8 -*-
"""
    task.utils
    ~~~~~~~~~~
    
    :copyright: (c) 2013 by Abhinav Singh.
    :license: BSD, see LICENSE for more details.
"""

def import_path(path): # pragma: no cover
    parts = path.split('.')
    prefix = '.'.join(parts[:-1])
    suffix = '.'.join(parts[-1:])
    method = suffix if suffix is not '*' else [suffix]
    
    try:
        module = __import__(prefix, globals(), locals(), method, -1)
        return getattr(module, method) if suffix is not '*' else module
    except AttributeError, e:
        raise ImportError(e)
