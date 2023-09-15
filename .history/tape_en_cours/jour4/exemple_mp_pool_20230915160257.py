from multiprocessing import Pool
import os 
import time

y = 1

def f(x):
    global y 
    print(x, os.getpid(), y)
    time.sleep(10)
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, range(20)))
