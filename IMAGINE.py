import tweepy
import keys
from tkinter import Tk, Canvas, Label, Entry, Button,filedialog,Frame

root = Tk()
root.geometry("700x500+500+500")
root.maxsize(height=400,width=500)
root.title("IMAGINE v1.0")
def submit():
    def api():
        auth = tweepy.OAuthHandler(keys.apikey,keys.apisecret)
        auth.set_access_token(keys.accesstoken,keys.accesstokensecret)

        return tweepy.API(auth)

    def tweet(api: tweepy.API,message:str,image_path=None):
        if image_path:
            api.update_status_with_media(message, image_path)
        else:
            api.update_status(message)



    
    input_text = input_field.get()
    input_text2 = input_field2.get()
    if len(input_text) > 0:
        if len(input_text2) > 0:
            api = api()
            tweet(api, input_text,input_text2)
            print(input_text2)
        else:
            api = api()
            tweet(api, input_text)
            print(input_text)
    else:
        print("no text in the box")
def getpath():
    file = filedialog.askopenfilename()
    setfile = input_field2.insert(0,file)
def retweet():
    def api():
        auth = tweepy.OAuthHandler(keys.apikey,keys.apisecret)
        auth.set_access_token(keys.accesstoken,keys.accesstokensecret)

        return tweepy.API(auth)
    
    
    def retweet(api: tweepy.API,retweetid: str):
        api.retweet(retweetid)
    id = retweetidfield.get()
    api = api()
    retweet(api,id)
def deletetweet():
    def api():
        auth = tweepy.OAuthHandler(keys.apikey,keys.apisecret)
        auth.set_access_token(keys.accesstoken,keys.accesstokensecret)

        return tweepy.API(auth)

    
    
    def deletetweetm(api: tweepy.API,retweetid: str):
        api.unretweet(id)
    id = deleletweetidfield.get()
    api = api()
    deletetweetm(api,id)

# info text    
infotxt = Label(text="Store all your keys in keys.py!")
infotxt.pack()
instructiontxt = Label(text="input the text you want to send")
instructiontxt.pack()
# text
input_field = Entry(root)
input_field.pack()
# Image Dir
pathbox = Label(text="image direction in here (optimal)")
pathbox.pack()
# file entry
input_field2 = Entry(root,)
input_field2.pack()
# buttons
submit_button = Button(root, text="send", command=submit,width=10, height=2,)
submit_button.pack()
getpath_button = Button(root, text="set image", command=getpath)
getpath_button.pack()
# Retweet
emptyfield = Label(root,text="--Retweet--")
emptyfield.pack()
retweetidfield = Entry(root)
retweetidfield.pack()
retweet_button = Button(root,text="retweet",command=retweet)
retweet_button.pack()
# delete retweet
deletetweet_field = Label(root,text="--delete retweet--")
deletetweet_field.pack()
deleletweetidfield = Entry(root)
deleletweetidfield.pack()
deletetweet_button = Button(root,text="delete retweet",command=deletetweet)
deletetweet_button.pack()
#instert text
retweetidfield.insert(0,string="Enter ID")
deleletweetidfield.insert(0,string="Enter ID")

root.mainloop()