import configparser
import os


class ConfigReader:

    def __init__(self):

        self.config = configparser.ConfigParser()

        config_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "config",
            "config.ini"
        )

        self.config.read(config_path)

    def get_url(self):
        return self.config["application"]["url"]

    def get_username(self):
        return self.config["login"]["username"]

    def get_password(self):
        return self.config["login"]["password"]