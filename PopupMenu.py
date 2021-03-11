"""
Author: rdbende
License: GNU GPLv3
Copyright (c): 2021 rdbende
"""

import tkinter as tk


class PopupMenu(tk.Menu):
    """A simple popup menu for Tkinter"""
    
    def __init__(self, master=None, **kwargs):
        """
        Create a tk.Menu
        
        Options:
            
            offsetx (int): the X offset popup relative to the cursor ()
            offsety (int): the Y offset relative to the cursor ()
            kwargs: options to be passed on to the tk.Menu initializer
             
        Generates:
        
            virtual event: <<PopupMenuPopup>> 
        """
        self._offx = kwargs.pop("offsetx", -2)
        self._offy = kwargs.pop("offsety", -2)
        tearoff = kwargs.pop("tearoff", False)
        tk.Menu.__init__(self, tearoff, **kwargs)
        self._master = master or tk._default_root
        if self._master.tk.call("tk", "windowingsystem") == "aqua":
            master.bind("<Button-2>", self._popup)
            master.bind("<Control-1>", self._popup)
        else:
            master.bind("<Button-3>", self._popup)
            
    def __getitem__(self, key):
        return self.cget(key)

    def __setitem__(self, key, value):
        self.configure(**{key: value})

    def _popup(self, event):
        try:
            self.tk_popup(int(event.x_root + self._offx), int(event.y_root + self._offy))
            self.event_generate("<<PopupMenuPopup>>")
        finally:
            self.grab_release()
            
    def add_submenu(self, *args, **kwargs):
        """Alias for add_cascade"""
        self.add_cascade(*args, **kwargs)
        
    def configure(self, **kwargs):
        """Configure resources of the widget."""
        self._offx = kwargs.pop("offsetx", self._offx)
        self._offy = kwargs.pop("offsety", self._offy)
        tk.Menu.configure(**kwargs)
        
    config = configure
    
    def cget(self, key):
        """Return the resource value for a KEY given as string"""
        if key == "offsetx":
            return self._offx
        elif key == "offsety":
            return self._offy
        else:
            return tk.Menu.cget(key)
    
    def keys(self):
        """Return a list of all resource names of this widget"""
        keys = tk.Menu.keys()
        keys.extend(["offsetx", "offsety"])
        keys.sort()
        return keys
