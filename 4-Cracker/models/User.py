
from models.Algorithms import Algorithms
# import datetime


class User:

    __user_list = []

    def __init__(self, password_string):
        # password_string format = name:$hashID$salt$hash:x:x:/user:/bin/bash
        # eg. root:$6$4Q8d4I.0$wRwdHdokUvq1oIsjQVncZIixSv3OzROYN8fJOs1BrklEuP2hrMAMLlSJ22EH/Rny4wLo1MmG1kuM6jyH713TR1:0:0:root:/root:/bin/bash
        name_split = password_string.split(':')
        password_split = name_split[1].split('$')

        self.name = name_split[0]
        self.hashId = password_split[1]
        self.salt = password_split[2]
        self.hash = password_split[3]
        self.password = ''

        self.__algorithm = Algorithms.get_algorithm(self.hashId)

    def verify(self, password):
        is_correct = self.__algorithm(self.hash, password, self.salt)
        # if is_correct:
            # print("Found passwd for user {} : {}".format(self.name, password))
            # print('timestamp: ', datetime.datetime.now())
            # self.password = password
        return is_correct

