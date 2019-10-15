
from models.User import User
from utils.FileManager import FileManager


class UserManager:

    __user_list = []

    @staticmethod
    def create_user(linux_password_string):
        new_user = User(linux_password_string)
        UserManager.__user_list.append(new_user)

    @staticmethod
    def remove_user(user):
        UserManager.__user_list.remove(user)

    @staticmethod
    def get_user_list():
        return UserManager.__user_list

    @staticmethod
    def populate_user_list_from_file(filepath):
        for linux_password_string in FileManager.get_file_lines(filepath):
            if linux_password_string.find(':$') > -1:
                UserManager.create_user(linux_password_string)

