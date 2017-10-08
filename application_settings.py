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
            self.tweet_frequency_minutes = parser.get('tweet_frequency', 'per_minutes')
            self.prime95_path = parser.get('prime95_location', 'path')
        except configparser.NoSectionError as ex:
            raise NoSectionError("Couldn't parse the config settings - Check the config.ini file exists and contains the [credentials] section") from ex


    def set_config_values(consumer_key, consumer_secret, access_token, access_secret, excitable, per_minutes, path):
        parser = configparser.ConfigParser()
        try:
            parser.read('config.ini')
            parser.set('credentials', 'consumer_key', consumer_key)
            parser.set('credentials', 'consumer_secret', consumer_secret)
            parser.set('credentials', 'access_token', access_token)
            parser.set('credentials', 'access_secret', access_secret)
            parser.set('tweet_style', 'excitable', excitable)
            parser.set('tweet_frequency', 'per_minutes', per_minutes)
            parser.set('prime95_location', 'path', path)

            self.consumer_key = parser.get('credentials', 'consumer_key')
            self.consumer_secret = parser.get('credentials', 'consumer_secret')
            self.access_token = parser.get('credentials', 'access_token')
            self.access_secret = parser.get('credentials', 'access_secret')
            self.tweets_are_excitable = parser.get('tweet_style', 'excitable')
            self.tweet_frequency_minutes = parser.get('tweet_frequency', 'per_minutes')
            self.prime95_path = parser.get('prime95_location', 'path')
            get_config_values()
        except configparser.NoSectionError as ex:
            raise NoSectionError("") from ex


    def get_config_values(self):
        parser = configparser.ConfigParser()
        try:
            self.consumer_key = parser.get('credentials', 'consumer_key')
            self.consumer_secret = parser.get('credentials', 'consumer_secret')
            self.access_token = parser.get('credentials', 'access_token')
            self.access_secret = parser.get('credentials', 'access_secret')
            self.tweets_are_excitable = parser.get('tweet_style', 'excitable')
            self.tweet_frequency_minutes = parser.get('tweet_frequency', 'per_minutes')
            self.prime95_path = parser.get('prime95_location', 'path')
            return self
        except configparser.NoSectionError as ex:
            raise configparser.NoSectionError("") from ex
