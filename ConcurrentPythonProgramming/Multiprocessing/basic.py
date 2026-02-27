import time
import multiprocessing
import concurrent.futures

def do_something(sec):
    print(f'Sleeping {sec} second...')
    time.sleep(sec)
    return (f'Done sleeping {sec}...')


if __name__ == '__main__':
    start = time.perf_counter()
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        sec = [9,8,7,6,5,4,3,2,1]
        result = [ executor.submit(do_something,s) for s in sec]
        
        for f in concurrent.futures.as_completed(result): print(f.result())

    # processes = []
    # for _ in range(10):
    #     p = multiprocessing.Process(target=do_something,args=[5])
    #     p.start()
    #     processes.append(p)
    
    # for process in processes: process.join()

    finish=time.perf_counter()

    print(f'Finished in {finish-start:.2f} seconds')