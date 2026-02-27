import asyncio

async def main():
    loop = asyncio.get_running_loop()
    future = loop.create_future()
    
    print("1. I am about to await the future...")
    
    # --- THE PROGRAM DIES HERE ---
    # It pauses here, expecting a result. 
    # But since we are paused, we can't write the code to set the result!
    result = await future 
    
    print("2. This line will NEVER print.")

if __name__ == "__main__":
    asyncio.run(main())