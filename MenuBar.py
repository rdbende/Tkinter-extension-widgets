"""
Author: rdbende
License: GNU GPLv3
Copyright (c): 2021 rdbende
"""

import tkinter as tk

class MenuBar(tk.Menu):
    """A simple menubar for Tkinter windows"""
    
    def __init__(self, master=None, tearoff=False, **kwargs):
        """
        Create a menubar
                
        Options:
            
            tearoff (bool): disables / enables tearoff of all menus and submenus (default is False / disabled)
            kwargs: options to be passed on to the tk.Menu initializer
            
        Methods:
        
            add_submenu: alias for add_cascade
            add_applemenu: creating Apple-icon menu on Mac
        """
        tk.Menu.__init__(self, **kwargs)
        try:
            master.option_add("*tearOff", tearoff)
            master.configure(menu=self)
        except:
            raise tk.TclError("The parent of the menubar must be a 'tk.Tk' or 'tk.Toplevel' instance")
        
    def add_submenu(self, *args, **kwargs):
        """Alias for add_cascade"""
        self.add_cascade(*args, **kwargs)
            
    def add_applemenu(self, *args, **kwargs):
        kwargs.update({"name" : "apple"})
        self.apple_menu = tk.Menu(self, *args, **kwargs)
        self.add_cascade(menu=self.apple_menu)
        
