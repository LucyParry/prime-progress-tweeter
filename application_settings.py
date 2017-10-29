import configparser

class AppSettings:
    """
    """
    def __init__(self, config_file_path):
        parser = configparser.ConfigParser()
        try:
            parser.read(config_file_path)
            self.consumer_key = parser.get('settings', 'consumer_key')
            self.consumer_secret = parser.get('settings', 'consumer_secret')
            self.access_token = parser.get('settings', 'access_token')
            self.access_secret = parser.get('settings', 'access_secret')
            self.tweets_are_excitable = parser.get('settings', 'tweets_excitable')
            self.tweet_frequency = parser.get('settings', 'tweet_frequency_cmd')
            self.prime95_path = parser.get('settings', 'prime95_location_path')
            self.frequency_options_dict = {"Hour": "/sc HOURLY", "3 hours": "/sc HOURLY /mo 3", "6 hours": "/sc HOURLY /mo 6", "12 hours": "/sc HOURLY /mo 12", "Day": "/sc DAILY"}
            self.style_options_dict = {"Excitable": "True", "Just the facts": "False"}

        except configparser.NoSectionError as ex:
            raise NoSectionError("Couldn't parse the config settings - Check the config.ini file exists and contains the [settings] section") from ex


    def set_config_values(self, str_consumer_key, str_consumer_secret, str_access_token, str_access_secret, str_excitable, str_frequency_cmd, str_path):
        parser = configparser.RawConfigParser()
        try:
            parser.read('config.ini')
            parser.set('settings', 'access_secret', str_access_secret)
            parser.set('settings', 'access_token', str_access_token)
            parser.set('settings', 'consumer_secret', str_consumer_secret)
            parser.set('settings', 'consumer_key', str_consumer_key)
            parser.set('settings', 'tweets_excitable', str_excitable)
            parser.set('settings', 'tweet_frequency_cmd', str_frequency_cmd)

            with open('config.ini', 'w') as configfile:
                parser.write(configfile)

        except configparser.NoSectionError as ex:
            raise NoSectionError("") from ex
