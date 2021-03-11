"""
Author: rdbende
License: GNU GPLv3
Copyright (c): 2021 rdbende
"""

# Based on RedFantom's ToggledFrame:
# https://github.com/RedFantom/ttkwidgets/blob/master/ttkwidgets/frames/toggledframe.py

import tkinter as tk
from tkinter import ttk as ttk

class ToggledFrame(ttk.Frame):
    """A collapsible and expandable frame for tkinter"""
    
    def __init__(self, master=None, **kwargs):
        """
        Create a ToggledFrame
                
        ToggledFrame options:
            
            text (str): the text shown on the expander button
            width (int): the width of the expander button given in characters
            cursor (str): the expander button's cursor
            expanded (bool): determines whether the frame is expanded by default
            kwargs: kwargs: options to be passed on to the ttk.Frame initializer
            
        Generates:
            
            virtual event: <<ToggledFrameToggled>>
            virtual event: <<ToggledFrameExpanded>>
            virtual event: <<ToggledFrameCollapsed>>
            
        Method:
            
            toggle : expand / collapse the frame
            
        Variable:
        
            state: expanded / collapsed
        """
        self._expanded = kwargs.pop("expanded", False)
        self._text = kwargs.pop("text", None)
        self._cursor = kwargs.pop("cursor", "arrow")
        self._width = kwargs.pop("width", 20)
        self._toggled = tk.BooleanVar(value=self._expanded)
        ttk.Frame.__init__(self, master, **kwargs)
        self._button = ttk.Checkbutton(self, style="Toolbutton", cursor=self._cursor,
                                       variable=self._toggled, command=self.toggle,
                                       text=self._text, width=self._width)
        self._button.grid(row=0, column=0, sticky="new")
        self.frame = ttk.Frame(self)
        self.state = "collapsed"
        if self._expanded:
            self.toggle()

    def toggle(self, *args):
        """Expand or collapse the frame"""
        if self.state == "expanded":
            self._toggled.set(False)
            self.frame.grid_forget()
            self.state = "collapsed"
            self.event_generate("<<ToggledFrameCollapsed>>")
        else:
            self._toggled.set(True)
            self.frame.grid(row=1, column=0, sticky="nswe")
            self.state = "expanded"
            self.event_generate("<<ToggledFrameExpanded>>")
        self.event_generate("<<ToggledFrameToggled>>")
            
    def configure(self, **kwargs):
        self._expanded = kwargs.pop("expanded", self._expanded)
        self._text = kwargs.pop("text", self._text)
        self._cursor = kwargs.pop("cursor", self._cursor)
        self._width = kwargs.pop("width", self._width)
        self._button.configure(text=self._text, cursor=self._cursor, width=self._width)
        ttk.Frame.configure(self, **kwargs)
        if self._expanded:
            self.state = "collapsed"
            self.toggle()
        else:
            self.state = "expanded"
            self.toggle()
        
    config = configure
            
    def cget(self, key):
        """Return the resource value for a KEY given as string"""
        if key == "cursor":
            return self._cursor
        elif key == "expanded":
            return self._expanded
        elif key == "state":
            return self.state
        elif key == "text":
            return self._text
        elif key == "width":
            return self._width
        else:
            return ttk.Frame.cget(key)
    
    def keys(self):
        """Return a list of all resource names of this widget"""
        keys = ttk.Frame.keys()
        keys.extend(["cursor", "text", "width"])
        keys.sort()
        return keys
