import threading
#from cse251functions import *

# This global variable keeps track of the final product
PRODUCT = 0

# This function computes the product of all numbers from 1 to the given number
def compute_product(number):
    global PRODUCT  # Declares that we're using the global variable PRODUCT
    product = 1  # Initializes the local variable to store product calculations
    for i in range(1, number):  # Loop from 1 to (number - 1) to calculate the product
        product *= i  # Multiplies current value by i and store back in product
    PRODUCT = product  # Assigns the computed value to the global variable PRODUCT

def main():
    global PRODUCT  # Declares that we're using the global variable PRODUCT

    # Creates a thread to run the compute_product function with argument 5
    thread1 = threading.Thread(target=compute_product, args=(5,))
    thread1.start()  # Starts the thread
    thread1.join()  # Waits until the thread completes

    # Asserts to check if the PRODUCT calculated for 5 is correct (1 * 2 * 3 * 4 = 24)
    assert PRODUCT == 24, f'The product should equal 24 but instead was {PRODUCT}'

    # Creates a thread to run the compute_product function with argument 10
    thread2 = threading.Thread(target=compute_product, args=(10,))
    thread2.start()  # Start the thread
    thread2.join()  # Wait until the thread completes

    # Asserts to check if the PRODUCT calculated for 10 is correct (1 * 2 * ... * 9 = 362880)
    assert PRODUCT == 362880, f'The product should equal 362880 but instead was {PRODUCT}'

    # Creates a thread to run the compute_product function with argument 15
    thread3 = threading.Thread(target=compute_product, args=(15,))
    thread3.start()  # Starts the thread
    thread3.join()  # Waits until the thread completes

    # Asserts to check if the PRODUCT calculated for 15 is correct (1 * 2 * ... * 14 = 87178291200)
    assert PRODUCT == 87178291200, f'The product should equal 87178291200 but instead was {PRODUCT}'

if __name__ == '__main__':
    main()  
    print("DONE")  # Print DONE if all asserts pass
