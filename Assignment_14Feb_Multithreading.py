# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 15:12:25 2023

@author: y0vwts9
"""
# Q1. What is multithreading in python? WHy it is used? Name the module used to 
#     handle threads in pyhton.
# Ans.
#     Multithreading refers to concurrently executing multiple threads by rapidly 
#     switching the control of the CPU between threads (called context switching). 

#     Why multithreading is used
#     Multithreading allows the programmer to divide application tasks into sub-tasks 
#     and simultaneously run them in a program. It allows threads to communicate and 
#     share resources such as files, data, and memory to the same processor.

#     Module used to handle threads in pyhton is threading.

# Q2. Why threading module is used? Write the use of the following functions:
#     1. activeCount(); 2. currentThread(); 3. enumerate()
# Ans.
#     Threading module allows you to have different parts of your process run concurrently.
#     1. activeCount():- It returns the number of active threads in the current 
#        thread's thread group. The value returned is only an estimate because 
#        the number of threads may change dynamically while this method traverses 
#        internal data structures.
#     2. currentThread():- This function is used to get a reference to the current 
#        thread object. It returns the thread object representing the thread from 
#        which it is called.
import threading
def my_function():
    print(f"Current thread: {threading.currentThread().getName()}")

t = threading.Thread(target=my_function)
t.start()
#     3. enumerate():- This function is used to get a list of all currently active 
#        Thread objects. It returns a list of thread objects representing the 
#        threads currently running.
import threading
def my_function():
    print("Thread started")

threads = []
for i in range(5):
    t = threading.Thread(target=my_function)
    threads.append(t)
    t.start()

for thread in threading.enumerate():
    print(f"Thread name: {thread.getName()}")

# Q3. Explain the following functions:-
#     1. run(); 2. start(); 3. join(); 4. isAlive()
# Ans.
#     run():- This function is the entry point for a thread when its start() 
#     method is called. It defines the code to be executed in the thread. 
import threading
def my_function():
    print("Hello from thread")

class MyThread(threading.Thread):
    def run(self):
        my_function()

t = MyThread()
t.start()

#     start():- This function starts a new thread by calling the run() method 
#     of the thread. When you call the start() method, it creates a new thread 
#     and then calls the run() method of the thread in a separate thread of execution.

#     join():- This function is used to block the calling thread until the thread 
#     whose join() method is called completes or terminates. If you call join() 
#     on a thread, the calling thread will wait until the specified thread 
#     completes its execution.

#     isalive():- This function is used to check whether a thread is currently 
#     executing or not. It returns True if the thread is currently executing, 
#     otherwise it returns False.

import threading
def my_function():
    print("Thread started")

t = threading.Thread(target=my_function)
print(f"Thread is alive: {t.is_alive()}")
t.start()
print(f"Thread is alive: {t.is_alive()}")
t.join()
print(f"Thread is alive: {t.is_alive()}")

# Q4. Write a python program to create two threads. Thread one must print the list
#     of squares and thread two must print the list of cubes.
import threading
def sq():
    print([i**2 for i in range(100)])
def tr():
    print([i**3 for i in range(10)])
s = threading.Thread(target = sq)
t = threading.Thread(target = tr)
s.start()
t.start()
s.join()
t.join()
print("Done")

# Q5. State advantages and disadvantages of multithreading.
# Ans.
#     Advantages:-
#     Enhanced performance by decreased development time
#     Simplified and streamlined program coding
#     Improvised GUI responsiveness
#     Simultaneous and parallelized occurrence of tasks
#     Better use of cache storage by utilization of resources
#     Decreased cost of maintenance
#     Better use of CPU resource

#     Disadvantages:-
#     Complex debugging and testing processes
#     Overhead switching of context
#     Increased potential for deadlock occurrence
#     Increased difficulty level in writing a program
#     Unpredictable results

# Q6. Explain deadlock and race conditions.
# Ans. 
#     A deadlock occurs when two threads each lock a different variable at the 
#     same time and then try to lock the variable that the other thread already 
#     locked. As a result, each thread stops executing and waits for the other 
#     thread to release the variable.

#     A race condition occurs when two threads access a shared variable at the 
#     same time. The first thread reads the variable, and the second thread reads 
#     the same value from the variable. Then the first thread and second thread 
#     perform their operations on the value, and they race to see which thread 
#     can write the value last to the shared variable. The value of the thread 
#     that writes its value last is preserved, because the thread is writing 
#     over the value that the previous thread wrote.




















