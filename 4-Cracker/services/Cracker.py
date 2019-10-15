
from utils.UserManager import UserManager
from utils.FileManager import FileManager
from utils.ProcessManager import ProcessManager
import math


class Cracker:

    __uncracked_users_list = []
    __dictionary = []

    @staticmethod
    def populate_uncracked_user_list(filepath):
        UserManager.populate_user_list_from_file(filepath)
        Cracker.__uncracked_users_list = UserManager.get_user_list()
        ProcessManager.update_pool(len(Cracker.__uncracked_users_list.copy()))

    @staticmethod
    def verify_password(password, user):
        if user.verify(password):
            print("\nFound passwd for user {} : {}".format(user.name, password))
            for user_in_list in Cracker.__uncracked_users_list:
                if user_in_list.name == user.name and user_in_list.hash == user.hash:
                    Cracker.__uncracked_users_list.remove(user_in_list)
                    break


    @staticmethod
    def get_dictionary(filepath):
        Cracker.__dictionary = FileManager.get_file_lines(filepath)


    @staticmethod
    def check_passwords_for_users(passwords):
        for password in passwords:
            ProcessManager.run_in_pool_2_inputs(Cracker.verify_password,
                                                [(password, x) for x in Cracker.__uncracked_users_list])

    @staticmethod
    def initiate_parallel_processing():
        chunk_size = math.ceil(len(Cracker.__dictionary)/ProcessManager.get_cpu_count())
        for i in range(0, len(Cracker.__dictionary), chunk_size):
            ProcessManager.create_new_process(Cracker.check_passwords_for_users,
                                              Cracker.__dictionary[i: i + chunk_size])
        ProcessManager.join_processes()

    @staticmethod
    def crack(dictionary, linux_password_file):
        Cracker.get_dictionary(dictionary)
        Cracker.populate_uncracked_user_list(linux_password_file)
        print('List of users: ', [x.name for x in Cracker.__uncracked_users_list.copy()])
        print('Dictionary size: ', len(Cracker.__dictionary))
        Cracker.initiate_parallel_processing()
        ProcessManager.kill_all_processes()
