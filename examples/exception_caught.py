from task import controller
from task.controllers import wait_until_done


@controller(wait_until_done)
def exc(t):
    raise Exception(t.args[0])


def raisesException(expected, func, *args, **kwargs):
    raised = False
    try:
        func(*args, **kwargs)
    except expected:
        raised = True
    except Exception:
        pass
    finally:
        return raised


if __name__ == "__main__":
    assert raisesException(Exception, exc, 'wtf')
