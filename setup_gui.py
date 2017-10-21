from tkinter import *

import prime_progress_tweeter
import application_settings

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

        app_settings = application_settings.AppSettings()

        tweet_styles_dict = app_settings.style_options_dict
        self.tweet_style_variable = StringVar()
        tweet_style_current = [name for (name, val) in tweet_styles_dict.items() if val == app_settings.tweets_are_excitable]
        self.tweet_style_variable.set(tweet_style_current[0])

        frequency_dict = app_settings.frequency_options_dict
        self.tweet_frequency_variable = StringVar()
        tweet_freq_current = [name for (name, val) in frequency_dict.items() if val == app_settings.tweet_frequency]
        self.tweet_frequency_variable.set(tweet_freq_current[0])
      
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

        
        image_frame = get_frame(self)

        image_gif = PhotoImage(file="assets/hen-311285_640.gif")
        image_label = Label(image_frame, image=image_gif, borderwidth=0)
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
        for item in tweet_styles_dict:
            Radiobutton(tweet_style_frame, text=item, padx = 10, variable=self.tweet_style_variable, value=[name for (name, val) in tweet_styles_dict.items() if name == item], font=("Helvetica", 10), background = background_theme).pack(side=LEFT)

        tweet_frequency_frame = get_frame(self)
        tweet_frequency_label = get_label(tweet_frequency_frame, "Tweet every")

        for item in frequency_dict:
            Radiobutton(tweet_frequency_frame, text=item, padx = 10, variable=self.tweet_frequency_variable, font=("Helvetica", 10), value=[name for (name, val) in frequency_dict.items() if name == item], background = background_theme).pack(side=LEFT)

        save_test_frame = Frame(self, background = background_theme)
        save_test_frame.pack(fill=X, pady=10, padx=150)

        def update_settings():
            consumer_key = consumer_key_entry.get()
            consumer_secret = consumer_secret_entry.get()
            access_token = access_token_entry.get()
            access_secret = access_secret_entry.get()
            tweet_style_selected = self.tweet_style_variable.get()
            tweet_frequency_selected = self.tweet_frequency_variable.get()

            tweet_style = [val for (name, val) in tweet_styles_dict.items() if name == tweet_style_selected]
            tweet_frequency = [val for (name, val) in frequency_dict.items() if name == tweet_frequency_selected]

            app_settings.set_config_values(consumer_key, consumer_secret, access_token, access_secret, tweet_style, tweet_frequency, "")

        save_button = Button(save_test_frame, font=("Helvetica", 11), text="Save", width=15, command=update_settings)
        save_button.pack(side=LEFT, padx=5, pady=5)

        test_button = Button(save_test_frame, font=("Helvetica", 11), text="Test tweet", width=15)
        test_button.pack(side=LEFT, padx=5, pady=5)


def main():
  
    root = Tk()
    root.geometry("600x600+150+150")
    app = PrimeTweeterGui()
    root.mainloop()  


if __name__ == '__main__':
    main()  