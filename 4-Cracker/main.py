
import sys
from os import path, getcwd
from services.Cracker import Cracker
# import datetime


if __name__ == '__main__':
    dictionary_file = sys.argv[1]
    linux_password_file = sys.argv[2]
    # print('Script started at: ', datetime.datetime.now())
    Cracker.crack(path.join(getcwd(), dictionary_file), path.join(getcwd(), linux_password_file))
    print('Done!')
