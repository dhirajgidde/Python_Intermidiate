
from threading import *
import time

class CheckThread(Thread):

    def run(self):
        time.sleep(1)
        if current_thread()==check_thread:
             for i in range(0,10):
                print(i)
        else:
            for i in range(11,20):
                print(i)


check_thread=CheckThread()
check_thread.start()

check_thread1=CheckThread()
check_thread1.start()
