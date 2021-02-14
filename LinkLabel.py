"""Simple clickable link widget for tkinter"""

import tkinter as tk
from tkinter import ttk
import webbrowser

class LinkLabel(ttk.Label):
    """
        A clickable label that opens a link
        
        Standard options:
            
            anchor, background, borderwidth, class
            compound, cursor, font, foreground, image
            justify, padding, relief, state, style, takefocus
            text, textvariable, underlinewidth, wraplength
                
        LinkLabel options:
            
            hovercolor (str): Color when you hover the label
            url (str): The link that you want to open
            visited (bool): Sets the link to be visited, it's false by default
            visitedcolor (str): Color after you clicked the label
            
        Generates:
        
            <<LinkOpened>>
            
        Variable:
        
            is_visited = True or False
            
        Usage:
        
            link = LinkLabel(master, text='Link', url='https://', hovercolor='#ff0000')
            link.pack()
    """
    
    def __init__(self, master=None, **kwargs):
        
        self._url = kwargs.pop("url", "https://")
        self._normalcolor = kwargs.pop("foreground", "#007fff")
        self._hovercolor = kwargs.pop("hovercolor", "#1133dd")
        self._visitedcolor = kwargs.pop("visitedcolor", "#6600aa")
        self._visited = kwargs.pop("visited", False)
        self.cursor = kwargs.pop("cursor", "hand2")
        ttk.Label.__init__(self, master, **kwargs)
        if "disabled" not in self.state():
            self.config(cursor=self.cursor, foreground=self._normalcolor)
        self.bind("<Button-1>", self._open)
        self.bind("<Enter>", self._enter)
        self.bind("<Leave>", self._leave)
        self.is_visited = self._visited
        self._leave()

    def _enter(self, *args):
        if "disabled" not in self.state():
            if self._visited:
                self.config(foreground=self._visitedcolor)
            else:
                self.config(foreground=self._hovercolor)

    def _leave(self, *args):
        if "disabled" not in self.state():
            if self._visited:
                self.config(foreground=self._visitedcolor)
            else:
                self.config(foreground=self._normalcolor)

    def _open(self, *args):
        """Opens the given url in the default webbrowser"""
        if "disabled" not in self.state():
            self._visited = True
            self.is_visited = True
            self.event_generate('<<LinkOpened>>')
            webbrowser.open(self._url)
            self._leave()

    def reset(self):
        """Clears the visited, and hovered statement"""
        self._visited = False
        self.is_visited = False
        self._leave()
    
    def cget(self, key):
        """Return the resource value for a KEY given as string"""
        if key is "url":
            return self._url
        elif key is "hovercolor":
            return self._hovercolor
        elif key is "visitedcolor":
            return self._visitedcolor
        elif key is "visited":
            return self._visited
        else:
            return ttk.Label.cget(self, key)    
    
    def keys(self):
        """Return a list of all resource names of this widget"""
        keys = ttk.Label.keys(self)
        keys.extend(["url", "hovercolor", "visitedcolor", "visited"])
        return keys

# Test

if __name__ == '__main__':
    
    root = tk.Tk()
    root.title('Link')
    root.geometry('200x70')
    
    def callback(event):
        print('Link clicked!')
        
    label = LinkLabel(root, url='https://github.com/rdbende/Tkinter-extension-widgets', text='Open link', font=('TkDefaultFont', 10, 'underline'))
    label.pack(pady=20)
    label.bind('<<LinkOpened>>', callback)
    
    root.mainloop()

