import math
import threading
import time
import sys

from PIL import Image

def create_signature_file():
    if SIS_ID == None or SIS_ID == '012345678':
        printError("Enter your SIS_ID in the resources/student_info.py file")

    if STUDENT_NAME == None or STUDENT_NAME == 'firstname.lastname':
        printError("Enter your first and last name in the resources/student_info.py file")

    width = 725
    height = 400

    char_count = 0
    word_count = 0
    line_count = 0
    frame = inspect.stack()[1]
    assignment_full_path = frame[0].f_code.co_filename
    if "prove" in assignment_full_path:
        print("grading...")
        return
    
    assignment_name = os.path.basename(assignment_full_path)
    
    with open(assignment_full_path, 'r') as f:
        for line in f:
            line_count += 1
            words = line.split()
            word_count += len(words)
            char_count += sum(len(word) for word in words)

    divide_index = 70
    if len(assignment_full_path) > divide_index:
        # find the nearest directory divider before the div_index characters
        for c in range(51, 0, -1):
            if assignment_full_path[c] == os.sep:
                divide_index = c
                break
        assignment_full_path = assignment_full_path[:divide_index] + '\n' + ' ' * 9 + assignment_full_path[divide_index:]
        
    text = f"Filename={assignment_full_path} \
            \nDATEIME={datetime.now()} \
            \nUUID={uuid.uuid4()} \
            \nNODE={uuid.getnode()} \
            \nLOGIN={os.getlogin()} \
            \nHOST={platform.node()} \
            \nARCH={platform.architecture()} \
            \nVERSION={platform.version()} \
            \nCORES={platform.processor()} \
            \nPROC={platform.machine()} \
            \n\nCharacters in {assignment_name[:-3]}={char_count} \
            \nWords in {assignment_name[:-3]}={word_count} \
            \nLines in {assignment_name[:-3]}={line_count} \
            \n\nSIS_ID={SIS_ID} \
            \nName={STUDENT_NAME} \
            \n\nOn my honor: \
            \n1. I wrote this myself\
            \n2. I have not copied any code from a current or previous student of CSE251 \
            \n3. I have added a comment to every line of code that I added to this assignment"
    filename = f'{SIS_ID}_{assignment_name[:-3]}_signature.jpeg'
    # get the absolute path to the directory this file exists in
    resource_path = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    # append the font name
    font_path =  os.path.join(resource_path, "COURBD.TTF")

    img = Image.new('CMYK', (width, height))
    draw1 = ImageDraw.Draw(img)
    font1 = ImageFont.truetype(font_path, 14)
    draw1.text((10, 15), text, (255, 255, 255), font=font1)
    img.save(filename)


# Global count of the number of primes found
total_primes = 0

# Global count of the numbers examined
total_numbers_checked = 0

# The number of threads to use (should try 1, 10, 50, and 101)
thread_count = 10

# The Lock synchronizes access to shared resources
lock = threading.Lock()

def check_prime(n: int) -> bool:
    """
    Check if a number is prime using a common optimization method.

    Primality test using 6k+-1 optimization.
    From: https://en.wikipedia.org/wiki/Primality_test

    Parameters
    ----------
    n : int
        Number to determine if prime.

    Returns
    -------
    bool
        True if n is prime, otherwise False.
    """
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Here there is a loop to check divisibility
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def compute_primes_in_range(start: int, end: int) -> None:
    """
    Count the number of primes in the given range and update global counters.

    Parameters
    ----------
    start : int
        Starting number of the range (inclusive).
    end : int
        Ending number of the range (exclusive).
    """
    global total_primes, total_numbers_checked

    # Local counters for the current thread
    local_prime_count = 0
    local_numbers_examined = 0

    # Iterates over range to check for primes
    for number in range(start, end):
        if check_prime(number):  # Checks if the current number is prime
            local_prime_count += 1  # Increases the  value of the local prime count
        local_numbers_examined += 1  # Increments the local numbers examined count

    with lock:  # This part is to ensure safe updates to global variables
        total_primes += local_prime_count  # Updates global prime count
        total_numbers_checked += local_numbers_examined  # Updates global numbers checked

def validate_inputs(first_number: int, interval: int, thread_count: int) -> None:
    """
    Validate the input parameters.

    Parameters
    ----------
    first_number : int
        Starting number for the range.
    interval : int
        Total count of numbers to examine.
    thread_count : int
        Number of threads to use.

    Raises
    ------
    ValueError
        If any input parameters are invalid.
    """
    if not isinstance(first_number, int) or first_number < 0:
        raise ValueError("First number must be a non-negative integer.")
    
    if not isinstance(interval, int) or interval <= 0:
        raise ValueError("Interval must be a positive integer.")
    
    if not isinstance(thread_count, int) or thread_count <= 0 or thread_count > 101:
        raise ValueError("Thread count must be a positive integer up to 101.")

def main():
    # Starts the timer to measure execution time
    begin_time = time.perf_counter()

    # Sets initial parameters
    first_number = 100_000_000  # The first number to start checking for primes
    interval = 370_803  # Total range of numbers to check
    last_number = first_number + interval  # Calculate thes last number in the range

    try:
        # Validates input parameters
        validate_inputs(first_number, interval, thread_count)

        # Calculates the size of each piece that each thread will handle
        chunk_size = interval // thread_count

        # Creates and starts threads
        threads = []  # This lis will hold the thread objects
        for i in range(thread_count):
            start = first_number + i * chunk_size  # Calculates starting number for the current thread
            # It ensures the last thread goes all the way to last_number
            end = last_number if i == thread_count - 1 else start + chunk_size  # Calculates ending number

            t = threading.Thread(target=compute_primes_in_range, args=(start, end))  # Creates a thread
            threads.append(t)  # Adds thread to the list
            t.start()  # Starts the thread

        # Waits for all threads to complete
        for t in threads:
            t.join()  # It ensures the main thread waits for the completion of each thread

        # Asserts session
        assert total_numbers_checked == 370_803, f"Should check exactly 370,803 numbers, but checked {total_numbers_checked:,}"
        assert total_primes == 20_144, f"Should find exactly 20,144 primes but found {total_primes:,}"

        # Prints out summary
        print(f'Numbers processed = {total_numbers_checked:,}')  # Prints total numbers processed
        print(f'Primes found = {total_primes:,}')  # Prints total primes found
        total_time = "{:.2f}".format(time.perf_counter() - begin_time)  # Calculates total time taken
        print(f'Total time = {total_time} sec')  # Prints total execution time

    except ValueError as e:
        print(f"Input Error: {e}")  # Prints input validation errors
        sys.exit(1)  # Exits the program with an error code


if __name__ == '__main__':
    main() 
    

