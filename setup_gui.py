#from tkinter import *

#class App:

#    def __init__(self, master):

#        background_theme = 'white'
#        root.title("The Prime Progress Tweeter")
        
#        root.configure(background = background_theme)

#        main_frame = Frame(root, height = 400, width = 400, background =
#        background_theme)
#        main_frame.pack_propagate(0)
#        main_frame.pack(padx = 5, pady = 5)

#        self.button = Button(main_frame, text="Exit", command=main_frame.quit)
#        self.button.pack(side=BOTTOM)

#        photo = PhotoImage(file="assets/hen-311185_640.gif")
#        label = Label(main_frame, image=photo)
#        label.image = photo
#        label.pack()

#        bottom_panel = Frame(self, relief=RAISED, borderwidth=1)
#        frame.pack(filedialog=BOTH, expand=true)

#        #consumer_key_label = Label(main_frame, text = "Consumer Key",
#        #background = background_theme, font=('', 11))
#        #consumer_key_label.pack()
#        #self.consumer_key_entry = Entry(main_frame)
#        #self.consumer_key_entry.pack()

#        #consumer_secret_label = Label(main_frame, text = "Consumer Secret",
#        #background = background_theme, font=('', 11))
#        #consumer_secret_label.pack()
#        #self.consumer_secret_entry = Entry(main_frame)
#        #self.consumer_secret_entry.pack()

#        #access_token_label = Label(main_frame, text = "Access Token",
#        #background = background_theme, font=('', 11))
#        #access_token_label.pack()
#        #self.access_token_entry = Entry(main_frame)
#        #self.access_token_entry.pack()

#        #access_secret_label = Label(main_frame, text = "Access Secret",
#        #background = background_theme, font=('', 11))
#        #access_secret_label.pack()
#        #self.access_secret_entry = Entry(main_frame)
#        #self.access_secret_entry.pack()

#        #self.hi_there = Button(main_frame, text="Hello", command=self.say_hi)
#        #self.hi_there.pack()

#    def say_hi(self):
#        print("hi there, everyone!")


#root = Tk()
#app = App(root)
#root.mainloop()
#root.destroy() # optional; see description below


#def main():
  
#    root = Tk()
#    root.geometry("500x500+500+500")
#    app = App(root)
#    root.mainloop()  


#if __name__ == '__main__':
#    main()  



from tkinter import *

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

        image_frame = Frame(self, background = background_theme)
        image_frame.pack(fill=X)

        image_gif = PhotoImage(file="assets/hen-311285_640.gif")
        image_label = Label(image_frame, image=image_gif, borderwidth=0)
        image_label.image = image_gif
        image_label.pack(padx=5, pady=5)

        intro_frame = Frame(self, background = background_theme)
        intro_frame.pack(fill=X)
        intro_text = "Enter your Twitter API credentials below"
        intro_label = Label(intro_frame, text=intro_text, font=("Helvetica", 11), justify=CENTER, background = background_theme)
        intro_label.pack(padx=10, pady=5)
      
        consumer_key_frame = Frame(self, background = background_theme)
        consumer_key_frame.pack(fill=X)        
        consumer_key_label = Label(consumer_key_frame, text="Consumer Key", width=15, justify=RIGHT, font=("Helvetica", 11, "bold"), anchor=W, background = background_theme)
        consumer_key_label.pack(side=LEFT, padx=5, pady=5)      
        consumer_key_entry = Entry(consumer_key_frame, background = entry_bkg_theme, font=("Helvetica", 11))
        consumer_key_entry.pack(fill=X, padx=5, expand=True)

        consumer_secret_frame = Frame(self, background = background_theme)
        consumer_secret_frame.pack(fill=X)        
        consumer_secret_label = Label(consumer_secret_frame, text="Consumer Secret", width=15, justify=RIGHT, font=("Helvetica", 11, "bold"), anchor=W, background = background_theme)
        consumer_secret_label.pack(side=LEFT, padx=5, pady=5)      
        consumer_secret_entry = Entry(consumer_secret_frame, background = entry_bkg_theme, font=("Helvetica", 11))
        consumer_secret_entry.pack(fill=X, padx=5, expand=True)
        
        access_token_frame = Frame(self, background = background_theme)
        access_token_frame.pack(fill=X)        
        access_token_label = Label(access_token_frame, text="Access Token", width=15, justify=RIGHT, font=("Helvetica", 11, "bold"), anchor=W, background = background_theme)
        access_token_label.pack(side=LEFT, padx=5, pady=5)      
        access_token_entry = Entry(access_token_frame, background = entry_bkg_theme, font=("Helvetica", 11))
        access_token_entry.pack(fill=X, padx=5, expand=True)
        
        access_secret_frame = Frame(self, background = background_theme)
        access_secret_frame.pack(fill=X)        
        access_secret_label = Label(access_secret_frame, text="Access Secret", width=15, justify=RIGHT, font=("Helvetica", 11, "bold"), anchor=W, background = background_theme)
        access_secret_label.pack(side=LEFT, padx=5, pady=5)      
        access_secret_entry = Entry(access_secret_frame, background = entry_bkg_theme, font=("Helvetica", 11))
        access_secret_entry.pack(fill=X, padx=5, expand=True)

        preferences_frame = Frame(self, background = background_theme)
        preferences_frame.pack(fill=X)
        preferences_text = "Enter your preferences below"
        preferences_label = Label(preferences_frame, text=preferences_text, font=("Helvetica", 11), justify=CENTER, background = background_theme)
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
        tweet_frequency_label.pack(side=LEFT, padx=5, pady=5)
        value_tweet_frequency = IntVar()
        value_tweet_frequency.set(1) 
        Radiobutton(tweet_frequency_frame, text="Hour", padx = 10, variable=value_tweet_style, font=("Helvetica", 10), value=1, background = background_theme).pack(side=LEFT)
        Radiobutton(tweet_frequency_frame, text="3 hours", padx = 10, variable=value_tweet_style, font=("Helvetica", 10), value=2, background = background_theme).pack(side=LEFT)
        Radiobutton(tweet_frequency_frame, text="6 hours", padx = 10, variable=value_tweet_style, font=("Helvetica", 10), value=2, background = background_theme).pack(side=LEFT)
        Radiobutton(tweet_frequency_frame, text="12 hours", padx = 10, variable=value_tweet_style, font=("Helvetica", 10), value=2, background = background_theme).pack(side=LEFT)
        Radiobutton(tweet_frequency_frame, text="Day", padx = 10, variable=value_tweet_style, value=2, font=("Helvetica", 10), background = background_theme).pack(side=LEFT)


        save_test_frame = Frame(self, background = background_theme)
        save_test_frame.pack(fill=X)

        save_button = Button(save_test_frame, font=("Helvetica", 11), text="Save")
        save_button.pack(side=LEFT)

        test_button = Button(save_test_frame, font=("Helvetica", 11), text="Test tweet")
        test_button.pack(side=LEFT)

        help_exit_frame = Frame(self, background = background_theme)
        help_exit_frame.pack(fill=X)

        help_button = Button(help_exit_frame, font=("Helvetica", 11), text="Help")
        help_button.pack(side=LEFT)

        exit_button = Button(help_exit_frame, font=("Helvetica", 11), text="Exit", command=self.quit)
        exit_button.pack(side=LEFT)



def main():
  
    root = Tk()
    root.geometry("600x600+150+150")
    app = PrimeTweeterGui()
    root.mainloop()  


if __name__ == '__main__':
    main()  