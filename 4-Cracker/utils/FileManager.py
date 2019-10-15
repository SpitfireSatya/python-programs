
class FileManager:

    @staticmethod
    def open_file(filepath):
        return open(filepath, 'r')

    @staticmethod
    def close_file(file_object):
        file_object.close()

    @staticmethod
    def get_file_lines(filepath):
        try:
            file_object = open(filepath, 'r')
            lines = file_object.read().splitlines()
            file_object.close()
            return lines
        except:
            print("Error reading lines")
            file_object.close()
