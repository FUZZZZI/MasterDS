# Q1. What is multiprocessing in python? Why is it useful?
# Ans.
#     Multiprocessing in Python is a technique of running multiple processes simultaneously 
#     within a single thread. It involves spawning multiple processes that 
#     run independently and can communicate with each other through inter-process 
#     communication mechanisms such as pipes, queues, and shared memory. Each process 
#     can have its own memory space and can execute tasks in parallel with other processes, 
#     which can lead to significant performance improvements for CPU-bound tasks.

# Q2. What are the differences between multiprocessing and multithreading?
# Ans.
#     Multithreading runs multiple threads simultaneously within a single process,
#     while multiprocessing runs multiple processes simultaneously within a single thread.

#     In Multiprocessing, Many processes are executed simultaneously. While in 
#     multithreading, many threads of a process are executed simultaneously.

#     Multiprocessing are classified into Symmetric and Asymmetric. 
#     While Multithreading is not classified in any categories.

#     In Multiprocessing, Process creation is a time-consuming process.
#     While in Multithreading, process creation is according to economical.

#     In Multiprocessing, every process owned a separate address space.
#     While in Multithreading, a common address space is shared by all the threads.

# Q3. Write a python code to create a process using the multiprocessing module.
# Ans.
def square(n):
    return n**2
if __name__ == "__main__":
    with multiprocessing.Pool(processes=5) as pool:
        out = pool.map(square, [3,4,5,6,7,78,8])
        print(out)
        
# Q4. What is a multiprocessing pool in python? Why is it used?
# Ans.
#     In Python, a multiprocessing pool is a way to parallelize the execution of 
#     a function across multiple input values. It allows you to distribute the 
#     workload across a specified number of processes that run in parallel, which 
#     can lead to significant performance improvements when executing CPU-bound tasks.

# Q5. How can we create a pool of worker processes in python using the multiprocessing module?
# Ans.
#     For example, suppose you have a function my_function that takes an input 
#     value and returns a result, and you want to apply it to a list of inputs 
#     my_inputs using a multiprocessing pool. You can create a pool of worker 
#     processes as follows:
import multiprocessing
pool = multiprocessing.Pool(processes=4)
#     This creates a pool with 4 worker processes. You can then apply the 
#     function to the list of inputs using the map method:
results = pool.map(my_function, my_inputs)

# Q6. Write a python program to create 4 processes, each process should print 
#     a different number using the multiprocessing module in python.
import multiprocessing

def print_number(number):
    print("Process {} prints: {}".format(multiprocessing.current_process().name, number))

if __name__ == '__main__':
    processes = []
    for i in range(4):
        p = multiprocessing.Process(target=print_number, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
