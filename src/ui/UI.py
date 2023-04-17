from tkinter import *
from tkinter import ttk



class Window(Tk):
    
    def __init__(self, title : str(), geometry : str(), resize : bool() ):
        '''
        title = "Title"
        grometry = 640x480
        resize = False
        '''
        super().__init__()
        self.title(title)
        self.geometry(geometry)
        self.resizable(resize, resize)
        self.mainloop()

class Frame(Frame):
    def __init__(self, owner):
        super().__init__()
        self.pack(owner)

class Button(Button):
    
    def __init__(self, owner, text = str()):
        """
        text = "Title" Название Кнопки
        owner = Window object
        Привязка к определённому окну
        """
        super().__init__()
        self(text)
        self.pack(owner)



    # def title(self, name : str()):
        # self.root.title(name)
        
    # def icon(self, type : str(), file = None):
        
        # if type == "ico":
            # self.root.iconbitmap(default=file)
        
        # elif type == "png":
            # icon = PhotoImage(file = file)
            # self.root.iconphoto(False, icon)
        
    # def size(self, size_x : str(), size_y : str()):
        # self.root.geometry(size_x + "x" + size_y)
    
    # def min_max_size(self, min_x : int(), min_y : int(), max_x : int(), max_y : int()):
        # '''
        # Ограничитель окна, 
        # устанавливаеться минимальный размер
        # и максимальный!
        # '''
        # self.root.minsize(min_x, min_y)
        # self.root.maxsize(max_x, max_y)
    
    # def resize(self, x_resize = bool(), y_resize = bool() ):
        # self.root.resizable(x_resize, y_resize)
    
    # def launch(self):
        # self.root.mainloop()
    
    # def close(self):
        # self.root.destroy()  # ручное закрытие окна и всего приложения
        
    # def print_info():
        # pass
    
    # def create_window(self, name, size_x, size_y, resizable):
        # self.root.title(name)
        # self.root.geometry(size_x + "x" + size_y)
        # self.root.resizable(resizable, resizable)
        # self.root.mainloop()
        
# Win = Window("Test", "640x480", False)

# Win.mainloop()

# Win.__doc__()

# Win.create_window("Test", "640", "480", False)

# Win.title("Half-Life 3")

# Win.icon("ico", "12.ico")
# Win.icon("png", "Pause3.png")

# Win.size("640", "480")

# Win.min_max_size(640, 480, 1200, 720)

# Win.launch()

root = Tk()



root.mainloop()