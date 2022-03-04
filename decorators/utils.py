import functools
import logging
import datetime as dt


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"i will start to execute the function very soon {args}")
        a, b = args
        if a > 100:
            print("a is a really big number, i do not wanto to calcuylate")
            return None
        result = func(*args, **kwargs)
        print(f"execution was successfull - the result is {result}")
        return result
    return wrapper


def log_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = dt.datetime.now()

        logging.error(f"{start}: {func.__name__} - START")
        result = func(*args, **kwargs)
        end = dt.datetime.now()
        logging.error(f"{end}: {func.__name__} - END -- RUNTIME = {(end - start).total_seconds()}s")
        return result
    return wrapper


def run_monitoring(func_object):
    def decorate(pipeline, *func_args):
        def call(func, *args, **kwargs):
            if not pipeline.run_config.get(func.__name__):
                pipeline.logger.info("Running method %s disabled in config." % func.__name__)
                return
            pipeline.logger.info("Method %s started." % func.__name__)
            result = func(pipeline, *args, **kwargs)
            pipeline.logger.info("Method %s finished." % func.__name__)
            return result

        return call(func_object, *func_args)

    return decorate
