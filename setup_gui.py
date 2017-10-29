from tkinter import *

import application_settings
import tweeter
import setup_task

class PrimeTweeterGui(Frame):
  
    def __init__(self):
        super().__init__()         
        self.initUI()

      
    def initUI(self):
      
        self.master.title("Prime Progress Tweeter")
        self.pack(fill=BOTH, expand=True)
        background_theme = "white"
        entry_bkg_theme = "gray95"
        self.configure(background = background_theme)

        app_settings = application_settings.AppSettings(sys.path[0] + '\config.ini')

        self.tweet_style_variable = StringVar()
        self.tweet_style_variable.set(app_settings.tweets_are_excitable)

        self.tweet_frequency_variable = StringVar()
        self.tweet_frequency_variable.set(app_settings.tweet_frequency)
      
        def get_frame(parent):
            frame = Frame(parent, background = background_theme)
            frame.pack(fill=X)
            return frame

        def get_label(parent, label_text):
            label = Label(parent, text=label_text, width=15, justify=RIGHT, font=("Helvetica", 11, "bold"), anchor=W, background = background_theme)
            label.pack(side=LEFT, padx=5, pady=5)
            return label

        def get_string_entry_variable(value):
            entry_var = StringVar()
            entry_var.set(value)
            return entry_var

        def get_string_entry(parent, variable):
            entry = Entry(parent, background = entry_bkg_theme, font=("Helvetica", 11), textvariable=variable)
            entry.pack(fill=X, padx=5, expand=True)
            return entry

        header_frame = get_frame(self)
        header_label = Label(header_frame, text="Prime Progress Tweeter", width=27, justify=RIGHT, font=("Helvetica", 20, "bold"), anchor=E, background = background_theme)
        header_label.pack(side=RIGHT, padx=5, pady=5)
        image_gif = PhotoImage(file="assets/hen-311285_640.gif")
        image_label = Label(header_frame, image=image_gif, borderwidth=0, justify=LEFT, anchor=W)
        image_label.image = image_gif
        image_label.pack(padx=5, pady=5)

        intro_frame = get_frame(self)
        intro_text = "Enter your Twitter API credentials below"
        intro_label = Label(intro_frame, text=intro_text, font=("Helvetica", 12, "bold"), justify=CENTER, background = background_theme)
        intro_label.pack(padx=10, pady=5)
            
        consumer_key_frame = get_frame(self)
        consumer_key_label = get_label(consumer_key_frame, "Consumer Key")
        consumer_key_entry_var = get_string_entry_variable(app_settings.consumer_key)
        consumer_key_entry = get_string_entry(consumer_key_frame, consumer_key_entry_var)

        consumer_secret_frame = get_frame(self)    
        consumer_secret_label = get_label(consumer_secret_frame, "Consumer Secret")
        consumer_secret_entry_var = get_string_entry_variable(app_settings.consumer_secret)       
        consumer_secret_entry = get_string_entry(consumer_secret_frame, consumer_secret_entry_var)
        
        access_token_frame = get_frame(self)      
        access_token_label = get_label(access_token_frame, "Access Token")
        access_token_entry_var = get_string_entry_variable(app_settings.access_token) 
        access_token_entry = get_string_entry(access_token_frame, access_token_entry_var)
        
        access_secret_frame = get_frame(self)    
        access_secret_label = get_label(access_secret_frame, "Access Secret")
        access_secret_entry_var = get_string_entry_variable(app_settings.access_secret)        
        access_secret_entry = get_string_entry(access_secret_frame, access_secret_entry_var)

        preferences_frame = Frame(self, background = background_theme)
        preferences_frame.pack(fill=X, pady=5)
        preferences_text = "Enter your preferences below"
        preferences_label = Label(preferences_frame, text=preferences_text, font=("Helvetica", 12, "bold"), justify=CENTER, background = background_theme)
        preferences_label.pack(padx=10, pady=5)

        tweet_style_frame = get_frame(self)
        tweet_style_label = get_label(tweet_style_frame, "Tweet style")
        for item in app_settings.style_options_dict.items():
            Radiobutton(tweet_style_frame, text=item[0], padx = 10, font=("Helvetica", 10), background = background_theme, 
                        variable=self.tweet_style_variable, value=item[1]).pack(side=LEFT)

        tweet_frequency_frame = get_frame(self)
        tweet_frequency_label = get_label(tweet_frequency_frame, "Tweet every")

        for item in app_settings.frequency_options_dict.items():
            Radiobutton(tweet_frequency_frame, text=item[0], padx = 10, font=("Helvetica", 10), background = background_theme, 
                        variable=self.tweet_frequency_variable, value=item[1]).pack(side=LEFT)


        def update_settings():
            consumer_key = consumer_key_entry.get()
            consumer_secret = consumer_secret_entry.get()
            access_token = access_token_entry.get()
            access_secret = access_secret_entry.get()
            tweet_style = self.tweet_style_variable.get()
            tweet_frequency = self.tweet_frequency_variable.get()
            app_settings.set_config_values(consumer_key, consumer_secret, access_token, access_secret, tweet_style, tweet_frequency, "")
            setup_task.create_or_update_task(tweet_frequency)

        save_test_frame = get_frame(self)
        save_test_frame.pack(fill=X, pady=10, padx=50)

        save_button = Button(save_test_frame, font=("Helvetica", 11), text="Save and start tweeting", width=20, command=update_settings)
        save_button.pack(side=LEFT, padx=5, pady=5)

        test_button = Button(save_test_frame, font=("Helvetica", 11), text="Send test tweet", width=15)
        test_button.pack(side=LEFT, padx=5, pady=5)

        stop_button = Button(save_test_frame, font=("Helvetica", 11), text="Stop tweeting", width=15)
        stop_button.pack(side=LEFT, padx=5, pady=5)


def main():  
    root = Tk()
    root.geometry("600x700+100+100")
    app = PrimeTweeterGui()
    root.mainloop()  


if __name__ == '__main__':
    main()  