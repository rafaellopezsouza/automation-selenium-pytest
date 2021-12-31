import os


class Credentials(object):
    def __init__(self):
        self.user = self.get_user()
        self.password = self.get_password()

    @staticmethod
    def get_user():
        return os.environ.get('USER')

    @staticmethod
    def get_password():
        return os.environ.get('PASSWORD')
