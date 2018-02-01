import configparser
import datetime
import os
import re
import subprocess
import sys
import tweepy

import application_settings
import exclamationator
import progress_finder


def setup_twitter_api(app_settings):
    """
    Sets up Tweepy API object, tests authorisation and returns the object if successful
    """
    try:
        auth = tweepy.OAuthHandler(app_settings.consumer_key, app_settings.consumer_secret)
        auth.set_access_token(app_settings.access_token, app_settings.access_secret)
        api = tweepy.API(auth)
        api.me() # test connection by attempting to get authorised user  
        return api        
    except tweepy.error.TweepError as ex:   # If the machine isn't online, just let Tweepy return the error
        raise tweepy.error.TweepError("Tweepy / Twitter API couldn't authenticate - Are you connected to the internet and are your API keys correct in the config.ini file?") from ex 


def tweet_message(api, message):
    """
    Tweet the given message
    """
    try:
        api.update_status(message)
    except tweepy.error.TweepError as ex:
        raise tweepy.error.TweepError("Tweepy encountered an error when sending the tweet") from ex 
    

def get_last_tweet_exponent(api):
    """
    Get the last tweet from the authorised user
    """
    try:
        last_tweet = api.home_timeline(count = 1)[0]
    except tweepy.error.TweepError as ex:
        raise tweepy.error.TweepError("Tweepy encountered an error when accessing the most recent tweet") from ex 
    match_exponent = re.search(r'M\d+', last_tweet.text)
    if (match_exponent):
        return match_exponent.group()
    else:
        return ""
    


def compose_progress_message(app_settings, percentage, exponentMString):
    """
    Build a standard tweet message about the prime progress
    """
    integer_exponent = exponentMString[1:]
    if not (is_integer(integer_exponent)):
        raise ValueError('Unable to parse integer from prime95 window title')
    else:
        superscript_exponent = integer_to_superscript(int(integer_exponent))        
        exclamation = ""
        if app_settings.tweets_are_excitable:
            exclamation = exclamationator.Exclamation(sys.path[0])
        message = exclamation.text + " We're " + percentage + " through calculating whether " + exponentMString + " (2" + superscript_exponent + "-1) might be prime!"
        if len(message) < 280:
            return message
        else:
            compose_progress_message(app_settings, percentage, exponentMString)


def compose_result_message(app_settings, resultString, completed_exponent):
    """
    Build a message about the result of an exponent 
    """
    integer_exponent = completed_exponent[1:]
    if not (is_integer(integer_exponent)):
        raise ValueError('Unable to parse integer from prime95 window title')
    else:
        superscript_exponent = integer_to_superscript(int(integer_exponent))
        exclamation = ""
        if app_settings.tweets_are_excitable:
            exclamation = exclamationator.Exclamation(sys.path[0], True)
            message = exclamation.text + " It turns out that" + " (2" + superscript_exponent + "-1) " + resultString + "!"
            if len(message) < 280:
                return message
            else:
                compose_result_message(app_settings, percentage, exponentMString)


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


def is_integer(string_integer):
    try:
        int(string_integer)
        return True
    except ValueError:
        return False


def write_error_to_logfile(message):
    if os.path.exists('error_log.txt'):
        with open("error_log.txt", "a") as myfile:
            myfile.write(str(datetime.datetime.now()) + ' - ' + message + '\n')
    else:
        with open("error_log.txt", "w") as myfile:
            myfile.write(str(datetime.datetime.now()) + ' - ' + message + '\n')


def do_progress_update(app_settings, api):
    """
    TODO - Write description
    """  
    try:
        progress_finder_obj = progress_finder.ProgressFinder()
        percentage, current_exponent = progress_finder_obj.get_progress_from_window_title()
        last_tweet_exponent = get_last_tweet_exponent(api)
        if (last_tweet_exponent != current_exponent) and last_tweet_exponent != "":
            # We have changed exponents between this check and the last one - Check what the verdict on the last one was instead
            do_completed_exponent_update(app_settings, api, last_tweet_exponent)

        message = compose_progress_message(app_settings, percentage, current_exponent)
        print(message)
        tweet_message(api, message)       
    except (IOError, ValueError, NotImplementedError, IndexError, tweepy.TweepError) as ex:
        write_error_to_logfile(str(ex))


def do_completed_exponent_update(app_settings, api, completed_exponent):
    """

    """
    # TODO - error handling
    try:
        results_path = app_settings.prime95_path
        exponent_result = ""
        with open(results_path) as file:
            for line in file:
                if completed_exponent in str(line):
                    exponent_result = line

        if len(exponent_result) > 0:
            exponent_result = (exponent_result.split(".")[0]).split(",")[1]
            message = compose_result_message(app_settings, exponent_result, completed_exponent)
            tweet_message(api, message)

    except configparser.NoSectionError as ex:
        raise NoSectionError("Couldn't parse the config settings - Check the config.ini file exists and contains the [credentials] section") from ex


def main():
    try:
        config_file_path = sys.path[0] + '\\' + 'config.ini'
        app_settings = application_settings.AppSettings(config_file_path)
        api = setup_twitter_api(app_settings)
    except (configparser.NoSectionError, tweepy.TweepError) as ex:
        write_error_to_logfile(str(ex))
    else:
        do_progress_update(app_settings, api)


if __name__ == '__main__':
   main()