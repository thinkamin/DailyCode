import tkinter as tk
from datetime import datetime
import subprocess
import random
from pathlib import Path
import time
import tkinter.messagebox as tm


class Root(tk.Tk):
    '''
    这个类里面只能放widget和要绑定的func
    '''
    def __init__(self,string):
        super().__init__()
    
        self.string = string
        # self.name = name
        self.label = tk.Label(self, text='', padx=10, pady=10,font='Monotye\ Corsiva -20 bold')
        self.label.pack()
        self.label = tk.Label(self, text=self.string, padx=10, pady=10,font='Monotye\ Corsiva -20 bold',wraplength=500,justify='center') #要折行后的对齐
        self.label.pack()
    
    def config(self):
        self.title('')
        # self.resizable(False,False)
        print(self.winfo_screenwidth(),self.winfo_screenheight())
        self.geometry('widthxheight')
        # 设置全屏
        #self.attributes('-fullscreen',True)
        # 置顶
        # root.wm_attributes('-topmost',1)



