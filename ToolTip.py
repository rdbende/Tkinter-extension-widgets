"""Simple tooltip widget for tkinter"""

import tkinter as tk

class ToolTip(object):
    """
        A simple tooltip widget for tkinter
        
        Standard label options:
            
            anchor, background, borderwidth, class
            compound, cursor, font, foreground, image
            justify, padding, relief, state, style, takefocus
            text, textvariable, underlinewidth, wraplength

        Specific options:
            
            wait (int): Wait before appearing (in seconds)
            duration (int): Wait before disappearing (in seconds)
            direction (str): Direction relative to the parent. Directions: cursor, above, below, right, left
            ipadx (int): Inner X padding of the tooltip
            ipady (int): Inner Y padding of the tooltip
            
        Usage:
        
            tooltip = ToolTip(master, text='Info', background='#cccccc')
    """
    
    def __init__(self, master, **kwargs):
        self.master = master
        self._wait = int(kwargs.pop("wait", "1")) * 1000
        self._duration = int(kwargs.pop("duration", "10")) * 1000
        self._direction = kwargs.pop("direction", "cursor")
        self._relief = kwargs.pop("relief", "solid")
        self._bd = kwargs.pop("borderwidth", "1")
        self._ipadx = kwargs.pop("ipadx", "3")
        self._ipady = kwargs.pop("ipady", "1")
        self.kwargs = kwargs
        self.master.bind("<Enter>", self._enter)
        self.master.bind("<Leave>", self._hidetip)
        self.master.bind("<ButtonPress>", self._hidetip)
        
    def _enter(self, *args):
        self._toplevel = tk.Toplevel(self.master)
        self._toplevel.overrideredirect(True)
        self._toplevel.withdraw()
        self.id0 = self.master.after(self._wait, self._showtip)
        self.id1 = self.master.after(self._duration, self._hidetip)
        
    def _hidetip(self, *args):
        self.master.after_cancel(self.id0)
        self.master.after_cancel(self.id1)
        self._toplevel.destroy()

    def _showtip(self):
        self._toplevel.deiconify()
        label = tk.Label(self._toplevel, self.kwargs, relief=self._relief, borderwidth=self._bd)
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
        elif self._direction is "cursor":
            self.x = label.winfo_pointerx() + 10
            self.y = label.winfo_pointery() + 20
        self._toplevel.geometry("+{}+{}".format(self.x, self.y))
        
    def configure(self, **kwargs):
        self._wait = int(kwargs.pop("wait", "1")) * 1000
        self._duration = int(kwargs.pop("duration", "10")) * 1000
        self._direction = kwargs.pop("direction", "cursor")
        self._relief = kwargs.pop("relief", "solid")
        self._bd = kwargs.pop("borderwidth", "1")
        self._ipadx = kwargs.pop("ipadx", "3")
        self._ipady = kwargs.pop("ipady", "1")
        self.kwargs = kwargs
        
    config = configure
    
    def cget(self, key):
        """Return the resource value for a KEY given as string"""
        if key == "wait":
            return int(self._wait / 1000)
        elif key == "duration":
            return int(self._duration / 1000)
        elif key == "direction":
            return self._direction
        elif key == "ipadx":
            return self._ipadx
        elif key == "ipady":
            return self._ipady
        else:
            return self.kwargs.get(key)
    
    def keys(self):
        """Return a list of all resource names of this widget"""
        _label = tk.Label()
        keys = _label.keys()
        keys.extend(["wait", "duration", "direction", "ipadx", "ipady"])
        keys = sorted(keys)
        return keys

# Test

if __name__ == '__main__':
    
    root = tk.Tk()
    root.title('ToolTip')
    root.geometry('220x70')

    button = tk.Button(root, text='Button', command=root.destroy)
    button.pack(pady=20)

    tooltip = ToolTip(button, text='Info')
    
    root.mainloop()
