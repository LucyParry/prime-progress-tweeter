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

        image_frame = Frame(self, background = background_theme)
        image_frame.pack(fill=X)

        image_gif = PhotoImage(file="assets/hen-311285_640.gif")
        image_label = Label(image_frame, image=image_gif, borderwidth=0)
        image_label.image = image_gif
        image_label.pack(padx=5, pady=5)

        intro_frame = Frame(self, background = background_theme)
        intro_frame.pack(fill=X)
        intro_text = "Enter your Twitter API credentials below"
        intro_label = Label(intro_frame, text=intro_text, font=("Helvetica", 12, "bold"), justify=CENTER, background = background_theme)
        intro_label.pack(padx=10, pady=5)
      
        consumer_key_frame = Frame(self, background = background_theme)
        consumer_key_frame.pack(fill=X)        
        consumer_key_label = Label(consumer_key_frame, text="Consumer Key", width=15, justify=RIGHT, font=("Helvetica", 11, "bold"), anchor=W, background = background_theme)
        consumer_key_label.pack(side=LEFT, padx=5, pady=5)
        consumer_key_entry_var = StringVar()
        consumer_key_entry_var.set(app_settings.consumer_key)
        consumer_key_entry = Entry(consumer_key_frame, background = entry_bkg_theme, font=("Helvetica", 11), textvariable=consumer_key_entry_var)
        consumer_key_entry.pack(fill=X, padx=5, expand=True)

        consumer_secret_frame = Frame(self, background = background_theme)
        consumer_secret_frame.pack(fill=X)        
        consumer_secret_label = Label(consumer_secret_frame, text="Consumer Secret", width=15, justify=RIGHT, font=("Helvetica", 11, "bold"), anchor=W, background = background_theme)
        consumer_secret_label.pack(side=LEFT, padx=5, pady=5)
        consumer_secret_entry_var = StringVar()
        consumer_secret_entry_var.set(app_settings.consumer_secret)       
        consumer_secret_entry = Entry(consumer_secret_frame, background = entry_bkg_theme, font=("Helvetica", 11), textvariable=consumer_secret_entry_var)
        consumer_secret_entry.pack(fill=X, padx=5, expand=True)
        
        access_token_frame = Frame(self, background = background_theme)
        access_token_frame.pack(fill=X)        
        access_token_label = Label(access_token_frame, text="Access Token", width=15, justify=RIGHT, font=("Helvetica", 11, "bold"), anchor=W, background = background_theme)
        access_token_label.pack(side=LEFT, padx=5, pady=5)
        access_token_entry_var = StringVar()
        access_token_entry_var.set(app_settings.access_token) 
        access_token_entry = Entry(access_token_frame, background = entry_bkg_theme, font=("Helvetica", 11), textvariable=access_token_entry_var)
        access_token_entry.pack(fill=X, padx=5, expand=True)
        
        access_secret_frame = Frame(self, background = background_theme)
        access_secret_frame.pack(fill=X)        
        access_secret_label = Label(access_secret_frame, text="Access Secret", width=15, justify=RIGHT, font=("Helvetica", 11, "bold"), anchor=W, background = background_theme)
        access_secret_label.pack(side=LEFT, padx=5, pady=5)
        access_secret_entry_var = StringVar()
        access_secret_entry_var.set(app_settings.access_secret)        
        access_secret_entry = Entry(access_secret_frame, background = entry_bkg_theme, font=("Helvetica", 11), textvariable=access_secret_entry_var)
        access_secret_entry.pack(fill=X, padx=5, expand=True)

        preferences_frame = Frame(self, background = background_theme)
        preferences_frame.pack(fill=X, pady=5)
        preferences_text = "Enter your preferences below"
        preferences_label = Label(preferences_frame, text=preferences_text, font=("Helvetica", 12, "bold"), justify=CENTER, background = background_theme)
        preferences_label.pack(padx=10, pady=5)

        tweet_style_frame = Frame(self, background = background_theme)
        tweet_style_frame.pack(fill=X)
        value_tweet_style = IntVar()
        value_tweet_style.set(1)
        tweet_style_label = Label(tweet_style_frame, text="Tweet style", width=15, justify=RIGHT, font=("Helvetica", 11, "bold"), anchor=W, background = background_theme)
        tweet_style_label.pack(side=LEFT, padx=5, pady=5)  
        Radiobutton(tweet_style_frame, text="Excitable", padx = 10, variable=value_tweet_style, font=("Helvetica", 10), value=1, background = background_theme).pack(side=LEFT)
        Radiobutton(tweet_style_frame, text="Just the facts", padx = 10, variable=value_tweet_style, font=("Helvetica", 10), value=2, background = background_theme).pack(side=LEFT)

        tweet_frequency_frame = Frame(self, background = background_theme)
        tweet_frequency_frame.pack(fill=X)
        tweet_frequency_label = Label(tweet_frequency_frame, text="Tweet every", width=15, justify=RIGHT, font=("Helvetica", 11, "bold"), anchor=W, background = background_theme)
        tweet_frequency_label.pack(side=LEFT, padx=5, pady=10)
        value_tweet_frequency = IntVar()
        value_tweet_frequency.set(1) 
        Radiobutton(tweet_frequency_frame, text="Hour", padx = 10, variable=value_tweet_style, font=("Helvetica", 10), value=1, background = background_theme).pack(side=LEFT)
        Radiobutton(tweet_frequency_frame, text="3 hours", padx = 10, variable=value_tweet_style, font=("Helvetica", 10), value=2, background = background_theme).pack(side=LEFT)
        Radiobutton(tweet_frequency_frame, text="6 hours", padx = 10, variable=value_tweet_style, font=("Helvetica", 10), value=2, background = background_theme).pack(side=LEFT)
        Radiobutton(tweet_frequency_frame, text="12 hours", padx = 10, variable=value_tweet_style, font=("Helvetica", 10), value=2, background = background_theme).pack(side=LEFT)
        Radiobutton(tweet_frequency_frame, text="Day", padx = 10, variable=value_tweet_style, value=2, font=("Helvetica", 10), background = background_theme).pack(side=LEFT)

        save_test_frame = Frame(self, background = background_theme)
        save_test_frame.pack(fill=X, pady=10, padx=150)

        save_button = Button(save_test_frame, font=("Helvetica", 11), text="Save", width=15)
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