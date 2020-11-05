import threading
from threading import *
import time

class MyThread(Thread):
    name = ""
    def __init__(self):
        Thread.__init__(self)


    def run(self):
        time.sleep(1)
        if (current_thread()==t1):
            for i in range(0,20):
                print(i)
        else:
            for i in range(21,40):
                print(i)




t1=MyThread()


t2=MyThread()

t1.start()
t1.join()
t2.start()