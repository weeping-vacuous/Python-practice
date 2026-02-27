import time
import asyncio

async def fetch_data(param):
    print(f"Do Domething wtih {param}")
    time.sleep(param)
    print(f"Done with {param}")
    return f"Result of {param}"

async def main():
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    result2 = await task2
    print("Task 2 fully completed")
    result = await task1
    print("Task 1 fully completed")
    return [result,result2]

t1 = time.perf_counter()
results = asyncio.run(main())
t2 = time.perf_counter()

print(f"Finshed in {t2-t1:.2f} seconds.")