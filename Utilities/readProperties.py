import configparser

config=configparser.RawConfigParser()
config.read('.\\Configuration\\config.ini')

class ReadConfig:
    @staticmethod
    def getApplicationurl():
        url=config.get('common info','baseurl')
        return url

    @staticmethod
    def getuseremail():
        email = config.get('common info', 'username')
        return email

    @staticmethod
    def getuserpaswd():
        passwd = config.get('common info', 'password')
        return passwd

