import configparser

class AppSettings:
    """
    """
    def __init__(self):
        parser = configparser.ConfigParser()
        try:
            parser.read('config.ini')
            self.consumer_key = parser.get('credentials', 'consumer_key')
            self.consumer_secret = parser.get('credentials', 'consumer_secret')
            self.access_token = parser.get('credentials', 'access_token')
            self.access_secret = parser.get('credentials', 'access_secret')
            self.tweets_are_excitable = parser.get('tweet_style', 'excitable')
            self.tweet_frequency = parser.get('tweet_frequency', 'frequency_cmd')
            self.prime95_path = parser.get('prime95_location', 'path')
            self.frequency_options_dict = {"Hour": "/sc HOURLY", "3 hours": "/sc HOURLY /mo 3", "6 hours": "/sc HOURLY /mo 6", "12 hours": "/sc HOURLY /mo 12", "Day": "/sc DAILY"}
            self.style_options_dict = {"Excitable": "True", "Just the facts": "False"}
        except configparser.NoSectionError as ex:
            raise NoSectionError("Couldn't parse the config settings - Check the config.ini file exists and contains the [credentials] section") from ex


    def set_config_values(self, str_consumer_key, str_consumer_secret, str_access_token, str_access_secret, str_excitable, str_frequency_cmd, str_path):
        parser = configparser.RawConfigParser()
        try:
            parser.read('config.ini')
            parser.set('credentials', 'access_secret', str_access_secret)
            parser.set('credentials', 'access_token', str_access_token)
            parser.set('credentials', 'consumer_secret', str_consumer_secret)
            parser.set('credentials', 'consumer_key', str_consumer_key)

            with open('config.ini', 'w') as configfile:
                parser.write(configfile)

        except configparser.NoSectionError as ex:
            raise NoSectionError("") from ex
