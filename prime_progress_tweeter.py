import configparser
import csv
import exclamationator
import subprocess
import tweepy
import re


def get_progress_from_window_title():
    """
    Runs a simple .bat file (which runs the Windows tasklist command) to get the task title of the prime95.exe process.
    This contains the current exponent and percentage done, which are return as a tuple if successful

    TODO - find out how to run the vbscript instead - should run the batch file without opening a cmd window
    """
    output = None
    win_title = ""
    try:
        output = subprocess.Popen(("get_window_name.bat"), stdout=subprocess.PIPE).stdout
        for line in output:
            if "Window Title" in str(line):
                win_title = str(line)
        if (len(win_title) > 0):  
            process_title = (win_title.split(" - ", 1)[1])
            percentage = process_title.split(" of ", 1)[0]
            exponent = process_title.split(" of ", 1)[1]
            exponent = exponent.split("\\", 1)[0]
            return (percentage, exponent)
        else:
            raise ValueError()
    except FileNotFoundError as ex:
        raise FileNotFoundError('Could not find the batch file get_window_name.bat - Has it been moved or renamed?') from ex
    except ValueError as ex:
        raise ValueError('No processes for prime95.exe found - Check the application is running') from ex
    finally:
        if not output is None:
            output.close()


def setup_twitter_api():
    """
    Reads Twitter credentials from .ini file, sets up API as a global variable and tests authorisation
    """
    parser = configparser.ConfigParser()
    try:
        parser.read('config.ini')
        consumer_key = parser.get('credentials', 'consumer_key')
        consumer_secret = parser.get('credentials', 'consumer_secret')
        access_token = parser.get('credentials', 'access_token')
        access_secret = parser.get('credentials', 'access_secret')

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        global api
        api = tweepy.API(auth)                         
        api.me() # test connection by attempting to get authorised user  

    except configparser.NoSectionError as ex:
        raise NoSectionError("Couldn't parse the config settings - Check the config.ini file exists and contains the [credentials] section") from ex
    except tweepy.error.TweepError as ex:
        raise tweepy.error.TweepError("Tweepy / Twitter API couldn't authenticate - Are your API keys correct in the config.ini file?") from ex 


def get_tweet_style():
    """
    Reads Tweet style from .ini file (whether we want a silly exclamation at the beginning or not)
    """
    parser = configparser.ConfigParser()
    parser.read('config.ini')
    tweet_style = parser.get('tweet_style', 'excitable')
    if tweet_style == "True":
        return True
    return False


def tweet_message(message):
    """
    Tweet the given message
    """ 
    api.update_status(message)


def get_last_tweet_exponent():
    """
    Get the last tweet from the authorised user
    """
    last_tweet = api.home_timeline(count = 1)[0]
    pattern = re.compile('M[0-9]*')
    match_exponent = pattern.search(last_tweet.text)
    last_tweet_exponent = match_exponent.group()
    return last_tweet_exponent


def compose_progress_message(percentage, exponentMString):
    """
    Build a standard tweet message about the prime progress
    """
    
    superscript_exponent = integer_to_superscript(int(exponentMString[1:]))
    exclamation = ""
    if get_tweet_style():
        exclamation = exclamationator.Exclamation()
    message = exclamation.text + " We're " + percentage + " through calculating whether " + exponentMString + " (2" + superscript_exponent + "-1) is prime!"
    if len(message) < 140:
        return message
    else:
        compose_message()


def integer_to_superscript(integer):
    """
    Converts each digit of a integer to equivalent unicode superscript character
    """
    uc_sup_digits_dict = {0: u"\u2070", 1: u"\u00B9", 2: u"\u00B2", 3: u"\u00B3", 4: u"\u2074",
                      5: u"\u2075", 6: u"\u2076", 7: u"\u2077", 8: u"\u2078", 9: u"\u2079"}
    int_string = str(integer)
    superscript = ""
    for i in range(len(int_string)):
        superscript = superscript + uc_sup_digits_dict[int(int_string[i])]
    return superscript


def do_progress_update():
    """
    TODO - Write description, handle exceptions (write to log file...)
    """  
    percentage, current_exponent = get_progress_from_window_title()
    last_tweet_exponent = get_last_tweet_exponent()
    if last_tweet_exponent != current_exponent:
        print("beep")
        # Ooh, we have changed exponents between this check and the last one - Check what the verdict on the last one was first
    message = compose_progress_message(percentage, current_exponent) 
    tweet_message(message)
    

if __name__ == '__main__':
    setup_result = setup_twitter_api()
    if setup_result == "OK":
        do_progress_update()
