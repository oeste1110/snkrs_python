from contextlib import contextmanager
import logging


@contextmanager
def counting(self, counter_name, start_from=0, step=1):
    counter = ProcessCounter(counter_name, start_from, step)
    yield counter
    logging.debug(counter.reg_report())


class ProcessCounter:
    def __init__(self, counter_name, start_from=0, step=1):
        self._counter_name = counter_name
        self._start_from = start_from
        self._counter = self._start_from
        self._step = step

    def incr(self):
        self._counter += self._step

    def decr(self):
        self._counter -= self._step

    def reg_report(self):
        return "{} 共处理 {} 项".format(self._counter_name,self._counter)


    def irreg_report(self):
        return "{} 计数为 {}".format(self._counter_name,self._counter)