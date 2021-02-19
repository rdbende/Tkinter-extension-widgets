"""A collapsible and expandable frame for tkinter"""

import tkinter as tk
from tkinter import ttk as ttk

class ToggledFrame(ttk.Frame):
    """
        A collapsible and expandable frame for tkinter
                
        ToggledFrame options:
            
            text (str): The text shown on the expander button
            width (int): The width of the expander button given in characters
            cursor (str): The expander button's cursor
            expanded (bool): Determines whether the frame is open by default
            
        Generates:
            
            <<ToggledFrameToggled>>
            <<ToggledFrameExpanded>>
            <<ToggledFrameCollapsed>>
            
        Method:
            
            toggle : expand or collapse the frame
            
        Variable:
        
            state : expanded or collapsed
            
        Usage:
        
            frame = ToggledFrame(master, text="Toggle", width=40, expanded=True)
            frame.pack()
            
            button = ttk.Button(frame.frame, text="Button")
            button.pack()
    """

    def __init__(self, master, **kwargs):
        self._expanded = kwargs.pop("expanded", False)
        self._text = kwargs.pop("text", "")
        self._cursor = kwargs.pop("cursor", "arrow")
        self._width = kwargs.pop("width", "20")
        self._toggled = tk.BooleanVar()
        self._toggled.set(self._expanded)
        ttk.Frame.__init__(self, master)
        self._button = ttk.Checkbutton(self, style='Toolbutton', cursor=self._cursor, command=self.toggle, variable=self._toggled, offvalue=False, onvalue=True, text=self._text, width=self._width)
        self._button.grid(row=0, column=0, sticky="new")
        self.frame = ttk.Frame(self)
        if self._expanded:
            self.toggle()

    def toggle(self):
        """Expand or collapse the frame"""
        self.event_generate("<<ToggledFrameToggled>>")
        if not self._toggled.get():
            self._toggled.set(False)
            self.frame.grid_forget()
            self.state = "collapsed"
            self.event_generate("<<ToggledFrameCollapsed>>")
        elif self._toggled.get():
            self._toggled.set(True)
            self.frame.grid(row=1, column=0, sticky="nswe")
            self.state = "expanded"
            self.event_generate("<<ToggledFrameExpanded>>")
            
    def cget(self, key):
        """Return the resource value for a KEY given as string"""
        if key == "text":
            return self._text
        elif key == "width":
            return self._extext
        elif key == "cursor":
            return self._cursor
        else:
            raise ValueError("ToggledFrame widget has no attribute '" + key + "'")
    
    def keys(self):
        """Return a list of all resource names of this widget"""
        keys = ["text", "width", "cursor"]
        return keys
    
# Test

if __name__ == '__main__':

    root = tk.Tk()
    root.title('ToggledFrame')
    
    def toggle_print(*args):
        print('Toggled')
    
    frame = ToggledFrame(root, text='Toggle', width=40)
    frame.pack()
    frame.bind('<<ToggledFrameToggled>>', toggle_print)
    
    def callback():
        print('Button clicked')
    
    button = ttk.Button(frame.frame, text='Button', command=callback)
    button.pack(pady=10)
    
    root.mainloop()
