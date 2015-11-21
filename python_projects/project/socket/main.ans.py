import asyncio
import sys

async def server_loop(reader, writer):
    while True:
        if reader.at_eof():
            return
        data = await reader.readline()
        print("Received {}".format(data.decode()))

que = asyncio.Queue()
async def client_loop():
    while True:
        try:
            reader, writer = (await 
                asyncio.open_connection(
                    '127.0.0.1', 3333
                )
            )
        except OSError:
            print("Server connect fail. retrying")
            await asyncio.sleep(1.0)
        else:
            break

    while True:
        s = await que.get()
        writer.write(s.encode())
        await asyncio.sleep(0.0)

def handle_stdin():
    data = sys.stdin.readline()
    que.put_nowait(data)

loop = asyncio.get_event_loop()
coro = asyncio.start_server(server_loop, 
                            '127.0.0.1',
                            3334)
loop.run_until_complete(coro)
loop.create_task(client_loop())
loop.add_reader(sys.stdin, handle_stdin)

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
