import concurrent.futures
import math
import os
import time

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]


def is_prime(n):
    try :
        pid = os.getpid()

        print("PID : {}, Checking is prime : {}".format(pid, n))
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False

        sqrt_n = int(math.floor(math.sqrt(n)))
        for i in range(3, sqrt_n + 1, 2):
            if n % i == 0:
                return False
        return True
    except OSError as err:
        print("-------------> OSError : {}".format(err))
    except Exception as e:
        print("-------------> Exception : {}".format(e))


def main():
    # with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    try:
        with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
            futures_dict = {}

            for number in range(1000):
                x = executor.submit(is_prime, number)
                futures_dict[number] = x

    except OSError as e:
        print("-------------> OSError : {}".format(e))
    except Exception as e:
        print("-------------> Exception : {}".format(e))

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("-------------> Exception : {}".format(e))