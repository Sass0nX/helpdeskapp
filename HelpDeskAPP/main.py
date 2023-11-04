from appfunction import *
from appmoduls import *


user = os.getlogin()

root = Tk()
hdapp = AppWindow(root, "Help Desk APP", '500x500','images\\favicon.ico', 'black')
hdapp.create_label("Help Desk APP", 10, 10)
hdapp.create_label(f'Hello {user}', 130, 10)
hdapp.create_button("Button", test, 'blue', 'white', 150, 150)
hdapp.create_window()
print(os.cpu_count())
