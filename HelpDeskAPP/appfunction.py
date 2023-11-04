#Functions
from appmoduls import *

def view():
    print('hello world')




def test():
    root2 = Tk()
    myapp = AppWindow(root2, "About me", '500x300', 'images\\favicon.ico')
    myapp.create_label('My plan is to make it easy for you!', 100, 100)
    myapp.create_button("contact with me", view ,150, 150)
    myapp.create_window()