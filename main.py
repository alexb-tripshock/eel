import eel
import os

eel.init("web") 

@eel.expose
def list_files():
    return os.listdir("./dir")

eel.start("index.html", size=(380, 700), port=80)