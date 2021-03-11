"""
Author: rdbende
License: GNU GPLv3
Copyright (c): 2021 rdbende
"""

# Based on RedFantom's LinkLabel: (https://github.com/RedFantom/ttkwidgets/blob/master/ttkwidgets/linklabel.py)

import tkinter as tk
from tkinter import ttk
import webbrowser

class LinkLabel(ttk.Label):
    """Clickable label that opens a link"""
    def __init__(self, master=None, **kwargs):
        """
        Create a clickable label

        Options:
        
            hovercolor (hex-color): text color when hovering over the widget
            normalcolor (hex-color): text color at the init of the widget
            url (str): the link to be open
            visited (bool): set the label to visited, (False by default)
            visitedcolor (hex-color): text color when link is clicked
            kwargs: options to be passed on to the ttk.Label initializer
            
        Generates:

            virtual event: <<LinkOpened>>
            
        Variable:
        
            is_visited: True or False
            
        Method:
            
            reset: reset the visited, and hovered statement
        """
        self._url = kwargs.pop("url", "https://")
        self._normalcolor = kwargs.pop("normalcolor", "#0007ff")
        self._hovercolor = kwargs.pop("hovercolor", "#00009f")
        self._visitedcolor = kwargs.pop("visitedcolor", "#660099")
        self.is_visited = kwargs.pop("visited", False)
        self._master = master or tk._default_root
        if self._master.tk.call("tk", "windowingsystem") == "aqua":
            self._cursor = kwargs.pop("cursor", "pointinghand")
        else:
            self._cursor = kwargs.pop("cursor", "hand2")
        ttk.Label.__init__(self, master, cursor=self._cursor, foreground=self._normalcolor, **kwargs)
        self.bind("<Button-1>", self._open)
        self.bind("<Enter>", self._enter)
        self.bind("<Leave>", self._leave)
        self._leave()

    def __getitem__(self, key):
        return self.cget(key)

    def __setitem__(self, key, value):
        self.configure(**{key: value})

    def _enter(self, *args):
        if self.is_visited:
            self.config(foreground=self._visitedcolor)
        else:
            self.config(foreground=self._hovercolor)

    def _leave(self, *args):
        if self.is_visited:
            self.config(foreground=self._visitedcolor)
        else:
            self.config(foreground=self._normalcolor)

    def _open(self, *args):
        """Open the given url in the default webbrowser"""
        webbrowser.open(self._url)
        self.is_visited = True
        self._leave()
        self.event_generate("<<LinkOpened>>")

    def reset(self):
        """Reset the visited, and hovered statement"""
        self.is_visited = False
        self._leave()

    def configure(self, **kwargs):
        """Configure resources of the widget"""
        self._url = kwargs.pop("url", self._url)
        self._normalcolor = kwargs.pop("normalcolor", self._normalcolor)
        self._hovercolor = kwargs.pop("hovercolor", self._hovercolor)
        self._visitedcolor = kwargs.pop("visitedcolor", self._visitedcolor)
        self.is_visited = kwargs.pop("visited", self.is_visited)
        self._cursor = kwargs.pop("cursor", self._cursor)
        ttk.Label.configure(self, cursor=self._cursor, **kwargs)

    config = configure
        
    def cget(self, key):
        """Return the resource value for a KEY given as string"""
        if key == "hovercolor":
            return self._hovercolor
        elif key == "normalcolor":
            return self._normalcolor
        elif key == "url":
            return self._url
        elif key == "visitedcolor":
            return self._visitedcolor
        elif key == "visited":
            return self.is_visited
        else:
            return ttk.Label.cget(self, key)    
    
    def keys(self):
        """Return a list of all resource names of this widget"""
        keys = ttk.Label.keys(self)
        keys.extend(["hovercolor", "normalcolor", "url", "visited", "visitedcolor", ])
        keys.sort()
        return keys
