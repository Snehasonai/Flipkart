from configparser import ConfigParser


def ConfigReader(section, Key):
    config = ConfigParser()
    config.read("C:\\BDDBehavePOM\\ConfigurationData\\config.ini")
    return config.get(section, Key)