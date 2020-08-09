import pickle
import os

class FileUtils:
    '''
    A utility class for machine learning
    '''

    @classmethod
    def save_to_file(cls, object, file_path):
        '''
        :param object: object where to be saved
        :param file_path: file_path where object should be saved
        :return:
        '''
        with open(file_path, 'wb') as f:
            pickle.dump(object, f, pickle.HIGHEST_PROTOCOL)

    @classmethod
    def load_from_file(cls, file_path):
        '''
        :param file_path: file path where object is saved
        :return: object loaded from file
        '''
        with open(file_path, 'rb') as f:
            return pickle.load(f)

    @classmethod
    def does_file_exists(cls, file_path):
        return os.path.exists(file_path)


