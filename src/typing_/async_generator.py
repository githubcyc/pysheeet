import asyncio

from typing import AsyncGenerator, AsyncIterator


async def fib(n: int) -> AsyncGenerator:
    a: int = 0
    b: int = 1
    while n > 0:
        await asyncio.sleep(0.1)
        yield a

        b, a = a + b, b
        n -= 1


async def main() -> None:
    async for f in fib(10):
        print(f)

    ag: AsyncIterator = (f async for f in fib(10))

    async for f in ag:
        print(f)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
