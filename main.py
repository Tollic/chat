import asyncio
import websockets

# Список подключенных клиентов
connected_clients = set()

async def connect_client(websocket, path):
    # Добавление клиента в список подключенных
    a = connected_clients.add(websocket)
    print(a)
    try:
        async for message in websocket:
            # Распространение сообщения по всем подключенным клиентам
            for client in connected_clients:
                await client.send(message)
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        # Удаление клиента из списка, если он отключился
        connected_clients.remove(websocket)

start_server = websockets.serve(connect_client, "localhost", 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
