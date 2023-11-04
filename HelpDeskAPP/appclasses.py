from appmoduls import *


class AppWindow:
    def __init__(self, root, title, size, path, bg):
        self.root = root
        self.size = size
        self.title = title
        self.path = path
        self.bg = bg

    def create_window(self):
        self.root.title(self.title)
        self.root.geometry(self.size)
        self.root.iconbitmap(self.path)
        self.root.configure(bg=self.bg)
        self.root.mainloop()

    def app_theme(self, theme):
        self.theme = theme
        self.style = ttk.Style(self.root)
        self.style.configure("Custom.TButton",
        foreground="black",
        background="white",
        padding=[10, 10, 10, 10],
        font="Verdana 12 underline")

    def create_label(self, content, x, y):
        self.content = content
        self.x = x
        self.y = y
        mylabel = ttk.Label(self.root, text=content, style='Custom.TButton')
        mylabel.place(x=x, y=y)

    def create_button(self, name, command, color1, color2 ,x, y):
        self.name = name
        self.command = command
        self.color1 = color1
        self.color2 = color2
        self.x = x
        self.y = y
        mybutton = tk.Button(self.root, text=name, command=command, bg=color1, fg=color2, activebackground='green')
        mybutton.place(x=x, y=y)

