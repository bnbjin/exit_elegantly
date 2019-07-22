# maintain lifecycle with asyncio

import asyncio

@asyncio.coroutine
def missionA():
    print('hello its mission A')
    print('mission A going to sleep...')

    yield from asyncio.sleep(1)

    print('A has awaken.')
    print('A is going to exit')

async def missionB():
    print('hi its mission B')
    print('mission B going to sleep...')

    await asyncio.sleep(2)

    print('B has awaken.')
    print('A is going to exit')

async def missionC():
    print('yo its mission C')
    print('and i never sleep!')


mission_list = [missionA(), missionB(), missionC()]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(mission_list))
loop.close()
