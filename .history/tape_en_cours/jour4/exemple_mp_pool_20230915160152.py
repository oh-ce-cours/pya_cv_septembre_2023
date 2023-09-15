from multiprocessing import Pool
import os 
import time

def f(x):
    print(x, os.getpid())
    time.sleep(10)
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, range(20)))
