import time


def sleep_it_generator(delay: int = 0):
    def real_sleep_it_generator(f):
        def wrapper(*args, **kwargs):
            for i in f(*args, **kwargs):
                time.sleep(delay)
                yield i

        return wrapper

    return real_sleep_it_generator


def sleep_it_ordinary(delay: int = 0):
    def real_sleep_it_ordinary(f):
        def wrapper(*args, **kwargs):
            time.sleep(delay)
            return f(*args, **kwargs)

        return wrapper

    return real_sleep_it_ordinary


class Rainbow:
    _colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', ]
    _length_loop = len(_colors)

    def __init__(self, circle: bool = True):
        self.circle = circle
        self.count = -1

    # @sleep_it_ordinary
    @sleep_it_generator(delay=3)
    def _get__colors(self) -> str:
        """
        yield colors in an infinite loop
        """
        i = 0
        while self.circle:
            yield self._colors[i]
            i += 1
            i %= len(self._colors)

    def __iter__(self):
        if self.circle:
            iterator = iter(self._get__colors())
        else:
            iterator = self
        return iterator

    # @sleep_it_generator
    @sleep_it_ordinary(delay=1)
    def __next__(self):
        if self.count < self._length_loop - 1:
            self.count += 1
            return self._colors[self.count]
        else:
            raise StopIteration


for color in Rainbow(circle=False):
    print(color)

print('-' * 10)

for color in Rainbow(circle=True):
    print(color)
