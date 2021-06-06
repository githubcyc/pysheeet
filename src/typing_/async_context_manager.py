import asyncio
from inspect import isawaitable, iscoroutinefunction


class AsyncCtxMgr:

    def do(self):
        print(f"do ... {iscoroutinefunction(self.__aexit__)}")

    async def __aenter__(self):
        await asyncio.sleep(3)
        print("__anter__")
        return self

    async def __aexit__(self, *exc):
        await asyncio.sleep(1)
        print("__aexit__")


async def hello():
    async with AsyncCtxMgr() as m:
        m.do()
        print("hello block")


async def world():
    print("world block")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    cor = world()
    print(isawaitable(cor))
    t = loop.create_task(cor)
    loop.run_until_complete(hello())
