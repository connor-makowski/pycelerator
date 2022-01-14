import time

class timeit:
    def __init__(self):
        self.start_time=None
        self.running=None

    def start(self, name='Total Process Time'):
        self.start_time=time.time()
        self.running=name

    def end(self):
        if self.running is None:
            raise Exception(f'`timeit` has not `start`ed yet')
        output=round(time.time()-self.start_time,4)
        name=self.running
        self.running=None
        self.start_time=None
        return f'{name}: {output} (seconds)'

timer=timeit()
