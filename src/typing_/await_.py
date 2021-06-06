import asyncio
from inspect import isawaitable, iscoroutine


class SlowObj:
    def __init__(self, n):
        print("__init__")
        self._n = n

    def __await__(self):
        print("__await__ sleep({})".format(self._n))
        yield from asyncio.sleep(self._n)
        print("ok")
        return self


async def main():
    obj = await SlowObj(1)
    print(type(obj))
    print(isawaitable(obj), iscoroutine(obj))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
