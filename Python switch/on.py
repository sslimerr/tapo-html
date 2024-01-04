import asyncio
from tapo import ApiClient

async def main():
    client = ApiClient("tapo-email", "tapo-password") # Set your Tapo password and email
    device = await client.p110("192.168.1.---") # Set your device IP

    await device.on()

asyncio.run(main())
