import threading
import time

class MyThread(threading.Thread):
    def run(self):
        for _ in range(5):
            print(threading.current_thread().getName(), "is running...")
            time.sleep(1)

#create two threads
thread1 = MyThread(name="Thread 1")
thread2 = MyThread(name="Thread 2")           

#Start Threads
thread1.start()
thread2.start()

#Wait for thread to complete
thread1.join()
thread2.join()

print("main thread exiting...")