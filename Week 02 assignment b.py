import threading
#from cse251functions import *

# Defines a class named ProductThread that extends the threading.Thread class
class ProductThread(threading.Thread):

    # Defines the constructor (__init__) method to initialize the class
    # Takes the number up to which the product must be calculated
    def __init__(self, number):
        threading.Thread.__init__(self)  # Calls the constructor of the parent (Thread) class
        self.number = number  # Stores the number argument in an instance variable
        self.product = 1  # Initializes the product attribute to 1

    # Defines the run method that will be executed when the thread starts
    def run(self):
        # Calculates the product of all numbers from 1 to (number - 1)
        for i in range(1, self.number):  # Iterates from 1 to (number - 1)
            self.product *= i  # Multiplies and accumulates the product

def main():
    # Instantiates a ProductThread object with the number 5 as argument
    thread1 = ProductThread(5)  # Calculates 1 * 2 * 3 * 4 = 24
    thread1.start()  # Starts the thread, invoking the run() method
    thread1.join()  # Waits for the thread to finish before continuing

    # Asserts that the product calculated by thread1 is equal to 24
    assert thread1.product == 24, f'The product should equal 24 but instead was {thread1.product}'

    # Instantiates a ProductThread object with the number 10 as argument
    thread2 = ProductThread(10)  # Calculates 1 * 2 * ... * 9 = 362880
    thread2.start()  # Starts the thread
    thread2.join()  # Waits for the thread to finish

    # Asserts that the product calculated by thread2 is equal to 362880
    assert thread2.product == 362880, f'The product should equal 362880 but instead was {thread2.product}'

    # Instantiates a ProductThread object with the number 15 as argument
    thread3 = ProductThread(15)  # Calculates 1 * 2 * ... * 14 = 87178291200
    thread3.start()  # Starts the thread
    thread3.join()  # Waits for the thread to finish

    # Asserts that the product calculated by thread3 is equal to 87178291200
    assert thread3.product == 87178291200, f'The product should equal 87178291200 but instead was {thread3.product}'

if __name__ == '__main__':
    main() 
    print("DONE")  # Prints DONE if all assertions pass
    