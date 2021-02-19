"""Simple clickable link widget for tkinter"""

import tkinter as tk
from tkinter import ttk
import webbrowser

class LinkLabel(ttk.Label):
    """
        A clickable label that opens a link
        
        Standard label options:
            
            anchor, background, borderwidth, class
            compound, cursor, font, foreground, image
            justify, padding, relief, state, style, takefocus
            text, textvariable, underlinewidth, wraplength
                
        Specific options:
            
            hovercolor (hex-color): Color when you hover the label
            url (str): The link that you want to open
            visited (bool): Sets the link to be visited, it's false by default
            visitedcolor (hex-color): Color after you clicked the label
            
        Generates:
        
            <<LinkOpened>>
            
        Variable:
        
            is_visited : True or False
            
        Method:
            
            clear : clears the visited, and hovered statement
            
        Usage:
        
            link = LinkLabel(master, text='Link', url='http://', hovercolor='#ff0000')
            link.pack()
    """
    
    def __init__(self, master, **kwargs):
        self._url = kwargs.pop("url", "https://")
        self._normalcolor = kwargs.pop("foreground", "#0007ff")
        self._hovercolor = kwargs.pop("hovercolor", "#00009f")
        self._visitedcolor = kwargs.pop("visitedcolor", "#6600aa")
        self._visited = kwargs.pop("visited", False)
        self._cursor = kwargs.pop("cursor", "hand2")
        self.is_visited = self._visited
        ttk.Label.__init__(self, master, **kwargs, cursor=self._cursor)
        self.bind("<Button-1>", self._open)
        self.bind("<Enter>", self._enter)
        self.bind("<Leave>", self._leave)
        self._leave()

    def _enter(self, *args):
        if self._visited:
            self.config(foreground=self._visitedcolor)
        else:
            self.config(foreground=self._hovercolor)

    def _leave(self, *args):
        if self._visited:
            self.config(foreground=self._visitedcolor)
        else:
            self.config(foreground=self._normalcolor)

    def _open(self, *args):
        """Opens the given url in the default webbrowser"""
        self._visited = True
        self.is_visited = self._visited
        self.event_generate('<<LinkOpened>>')
        webbrowser.open(self._url)
        self._leave()

    def clear(self):
        """Clears the visited, and hovered statement"""
        self._visited = False
        self.is_visited = self._visited
        self._leave()
        
    def cget(self, key):
        """Return the resource value for a KEY given as string"""
        if key == "url":
            return self._url
        elif key == "hovercolor":
            return self._hovercolor
        elif key == "visitedcolor":
            return self._visitedcolor
        elif key == "visited":
            return self._visited
        else:
            return ttk.Label.cget(self, key)    
    
    def keys(self):
        """Return a list of all resource names of this widget"""
        keys = ttk.Label.keys(self)
        keys.extend(["hovercolor", "url", "visited", "visitedcolor", ])
        keys = sorted(keys)
        return keys

# Test

if __name__ == '__main__':
    
    root = tk.Tk()
    root.title('LinkLabel')
    root.geometry('220x70')
    
    def callback(event):
        print('Link clicked!')
        
    label = LinkLabel(root, url='https://github.com/rdbende/Tkinter-extension-widgets', text='Open repo', font=('TkDefaultFont', 10, 'underline'))
    label.pack(pady=20)
    label.bind('<<LinkOpened>>', callback)
    
    root.mainloop()
