import asyncio
import sys

async def server_loop(reader, writer):
    raise NotImplementedError

async def client_loop():
    raise NotImplementedError

def handle_stdin():
    raise NotImplementedError

loop = asyncio.get_event_loop()


try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
