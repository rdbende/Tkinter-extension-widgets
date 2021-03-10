"""
Author: rdbende
License: GNU GPLv3
Copyright (c): 2021 rdbende
"""


import tkinter as tk

class ToolTip:
    """Popup help for Tkinter widgets"""

    def __init__(self, master, **kwargs):
        """
        Create a ToolTip
        
        :param wait: wait before appearing (in seconds)
        :type wait: int
        :param duration: wait before disappearing (in seconds)
        :type duration: int
        :param direction: direction relative to the parent
            directions: cursor, above, below, right, left (default is cursor)
        :type: str
        :param ipadx: inner X padding of the tooltip
        :type ipadx: int
        :param ipady: inner Y padding of the tooltip
        :type ipady: int
        :param kwargs: options to be passed on to the :class:`ttk.Label` initializer inside the tooltip
        """
        self.master = master
        self._text = kwargs.pop("text", None)
        self._wait = int(kwargs.pop("wait", "1")) * 1000
        self._duration = int(kwargs.pop("duration", "10")) * 1000
        self._direction = kwargs.pop("direction", "cursor")
        self._relief = kwargs.pop("relief", "solid")
        self._bd = kwargs.pop("borderwidth", "1")
        self._ipadx = kwargs.pop("ipadx", "3")
        self._ipady = kwargs.pop("ipady", "1")
        self.kwargs = kwargs
        if self._text is not None:
            self.master.bind("<Enter>", self._enter)
            self.master.bind("<Leave>", self._hidetip)
            self.master.bind("<ButtonPress>", self._hidetip)
        
    def __getitem__(self, key):
        return self.cget(key)

    def __setitem__(self, key, value):
        self.configure(**{key: value})
        
    def _enter(self, *args):
        """Initialize the :class:`tk.Toplevel`"""
        self._toplevel = tk.Toplevel(self.master)
        self._toplevel.overrideredirect(True)
        self._toplevel.withdraw()
        self.id0 = self.master.after(self._wait, self._showtip)
        self.id1 = self.master.after(self._duration, self._hidetip)
        
    def _hidetip(self, *args):
        """Destroy the tooltip"""
        self.master.after_cancel(self.id0)
        self.master.after_cancel(self.id1)
        self._toplevel.destroy()

    def _showtip(self):
        """Display the tooltip"""
        self._toplevel.deiconify()
        label = tk.Label(self._toplevel, text=self._text, relief=self._relief, borderwidth=self._bd, **self.kwargs)
        label.pack(ipadx=self._ipadx, ipady=self._ipady)
        if self._direction == "above":
            self.x = int(self.master.winfo_rootx() + (self.master.winfo_width() / 2) - (label.winfo_reqwidth() / 2))
            self.y = self.master.winfo_rooty() - label.winfo_reqheight() - 5
        elif self._direction == "below":
            self.x = int(self.master.winfo_rootx() + (self.master.winfo_width() / 2) - (label.winfo_reqwidth() / 2))
            self.y = self.master.winfo_rooty() + self.master.winfo_reqheight() + 5
        elif self._direction == "right":
            self.x = self.master.winfo_rootx() + self.master.winfo_width() + 5
            self.y = int(self.master.winfo_rooty()  + (self.master.winfo_height() / 2) - (label.winfo_reqheight() / 2))
        elif self._direction == "left":
            self.x = self.master.winfo_rootx() - label.winfo_reqwidth() - 5
            self.y = int(self.master.winfo_rooty()  + (self.master.winfo_height() / 2) - (label.winfo_reqheight() / 2))
        elif self._direction == "cursor":
            self.x = label.winfo_pointerx() + 10
            self.y = label.winfo_pointery() + 20
        self._toplevel.geometry("+{}+{}".format(self.x, self.y))
        
    def configure(self, **kwargs):
        """Configure resources of the widget."""
        self._text = kwargs.pop("text", None)        
        self._wait = int(kwargs.pop("wait", "1")) * 1000
        self._duration = int(kwargs.pop("duration", "10")) * 1000
        self._direction = kwargs.pop("direction", "cursor")
        self._relief = kwargs.pop("relief", "solid")
        self._bd = kwargs.pop("borderwidth", "1")
        self._ipadx = kwargs.pop("ipadx", "3")
        self._ipady = kwargs.pop("ipady", "1")
        self.kwargs = kwargs
        if self._text is not None:
            self.master.bind("<Enter>", self._enter)
            self.master.bind("<Leave>", self._hidetip)
            self.master.bind("<ButtonPress>", self._hidetip)
        
    config = configure
    
    def cget(self, key):
        """Return the resource value for a KEY given as string"""
        if key == "text":
            return self._text
        elif key == "wait":
            return int(self._wait / 1000)
        elif key == "duration":
            return int(self._duration / 1000)
        elif key == "direction":
            return self._direction
        elif key == "ipadx":
            return self._ipadx
        elif key == "ipady":
            return self._ipady
        elif key == "relief":
            return self._relief
        elif key == "borderwidth":
            return self._bd
        else:
            return self.kwargs.get(key)
    
    def keys(self):
        """Return a list of all resource names of this widget"""
        label = tk.Label()
        keys = label.keys()
        keys.extend(["wait", "duration", "direction", "ipadx", "ipady"])
        keys.sort()
        return keys

# Test

if __name__ == '__main__':
    
    root = tk.Tk()
    root.title('ToolTip')
    root.geometry('220x70')

    button = tk.Button(root, text='Button', command=root.destroy)
    button.pack(pady=20)

    tooltip = ToolTip(button)
    tooltip.config(text='bende')
    
    root.mainloop()
