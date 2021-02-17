import tkinter as tk
import tkinter.ttk as ttk
import os.path
import webbrowser


# Theme

class Theme(ttk.Style):
    """
        A theme widget for ttk to simply set the window's theme
                
        Options:
            
            file (str): Path to a tcl theme file
            name (str): The name of the theme
            pkg (str): Path to a folder containing pkgIndex.tcl and other tcl files
            
        Usage:
        
            If you only want to use one of ttk's built-in themes:
                theme = Theme(root, name='built in theme names e.g.: 'alt', 'clam', 'classic', 'default', 'aqua', 'vista', 'winnative', 'xpnative'')
                
            If you want to use a single tcl file (e.g. azure):
                theme = Theme(root, file='path to a tcl theme file')
                
            If you have a theme package (e.g. awthemes), you can use it with:
                theme = Theme(root, pkg='path to a theme package', name='name of theme you want to use')
                
    """

    def __init__(self, master=None, name=None, file=None, pkg=None):
        self._pkg = pkg
        self._name = name
        self._file = file
        self.master = master
        ttk.Style.__init__(self, master)
        if self._pkg != None:
            self.master.tk.call('lappend', 'auto_path', self._pkg)
            self.master.tk.call('package', 'require', os.path.basename(self._name))
        if self._file != None and self._name != None:
            raise Exception("Couldn't use theme name and tcl file at the same time")
        try:
            if self._file != None:
                self.master.tk.call('source', self._file)
                self.theme_use(os.path.basename(self._file).replace(".tcl", ""))
            else:
                self.theme_use(self._name)
        except Exception:
            raise Exception ("Something went wrong setting the theme")
        
    def cget(self, key):
        """Return the resource value for a KEY given as string"""
        if key is "name":
            return self._name
        elif key is "file":
            return self._file
        elif key is "pkg":
            return self._pkg
        else:
            raise ValueError("Theme widget has no attribute '" + key + "'")
    
    def keys(self):
        """Return a list of all resource names of this widget"""
        keys = ["name", "file", "pkg"]
        return keys



# ToolTip

class ToolTip(object):
    """
        A simple tooltip widget for tkinter
        
        Standard options:
            
            anchor, background, borderwidth, class
            compound, cursor, font, foreground, image
            justify, padding, relief, state, style, takefocus
            text, textvariable, underlinewidth, wraplength

        ToolTip options:
            
            wait (int): Waiting before appearing (s)
            duration (int): Waiting before disappearing (s)
            direction (str): Direction relative to the parent (above/below/right/left/cursor)
            ipadx (str): Inner X padding of the tooltip 
            ipady (str): Inner Y padding of the tooltip 
            
        Usage:
        
            tooltip = ToolTip(master, text='Info')
    """
    
    def __init__(self, master, wait=1, duration=10, direction="above", ipadx=1, ipady=1, **kwargs):
        self.master = master
        self._wait = int(wait * 1000)
        self._duration = int(duration * 1000)
        self._direction = direction
        self._relief = kwargs.pop("relief", "solid")
        self._bd = kwargs.pop("borderwidth", "1")
        self._ipadx = ipadx
        self._ipady = ipady
        self.kwargs = kwargs
        self.master.bind("<Enter>", self._enter)
        self.master.bind("<Leave>", self._hidetip)
        self.master.bind("<ButtonPress>", self._hidetip)
        
    def _enter(self, event=None):
        self._toplevel = tk.Toplevel(self.master)
        self._toplevel.overrideredirect(True)
        self._toplevel.withdraw()
        self.id0 = self.master.after(self._wait, self._showtip)
        self.id1 = self.master.after(self._duration, self._hidetip)
        
    def _hidetip(self, event=None):
        self.master.after_cancel(self.id0)
        self.master.after_cancel(self.id1)
        self._toplevel.destroy()

    def _showtip(self):
        self._toplevel.deiconify()
        label = tk.Label(self._toplevel, self.kwargs, relief=self._relief, borderwidth=self._bd)
        label.pack(ipadx=self._ipadx, ipady=self._ipady)
        if self._direction is "above":
            self.x = int(self.master.winfo_rootx() + (self.master.winfo_width() / 2) - (label.winfo_reqwidth() / 2))
            self.y = self.master.winfo_rooty() - label.winfo_reqheight() - 5
        elif self._direction is "below":
            self.x = int(self.master.winfo_rootx() + (self.master.winfo_width() / 2) - (label.winfo_reqwidth() / 2))
            self.y = self.master.winfo_rooty() + self.master.winfo_reqheight() + 5
        elif self._direction is "right":
            self.x = self.master.winfo_rootx() + self.master.winfo_width() + 5
            self.y = int(self.master.winfo_rooty()  + (self.master.winfo_height() / 2) - (label.winfo_reqheight() / 2))
        elif self._direction is "left":
            self.x = self.master.winfo_rootx() - label.winfo_reqwidth() - 5
            self.y = int(self.master.winfo_rooty()  + (self.master.winfo_height() / 2) - (label.winfo_reqheight() / 2))
        elif self._direction is "cursor":
            self.x = label.winfo_pointerx() + 10
            self.y = label.winfo_pointery() + 20
        self._toplevel.geometry("+{}+{}".format(self.x, self.y))
        
    def configure(self, wait=1, duration=10, direction="above", ipadx=1, ipady=1, **kwargs):
        self._wait = int(wait * 1000)
        self._duration = int(duration * 1000)
        self._direction = direction
        self._relief = kwargs.pop("relief", "solid")
        self._bd = kwargs.pop("borderwidth", "1")
        self._ipadx = ipadx
        self._ipady = ipady
        self.kwargs = kwargs
        
    config = configure
    
    def cget(self, key):
        """Return the resource value for a KEY given as string"""
        if key is "message":
            return self._msg
        elif key is "wait":
            return self._wait
        elif key is "duration":
            return self._duration
        elif key is "direction":
            return self._direction
        elif key is "ipadx":
            return self._ipadx
        elif key is "ipady":
            return self._ipady
        else:
            return tk.Label.cget(self, key)
    
    def keys(self):
        """Return a list of all resource names of this widget"""
        keys = tk.Label.keys(self)
        keys.extend["wait", "duration", "direction", "ipadx", "ipady"]
        return keys



# LinkLabel

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
        
            link = LinkLabel(master, text='Link', url='url', hovercolor='#ff0000')
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


# Image

class Image(tk.Label):
    """
        An image display widget for tkinter
                
        Image options:
            
            file (str): Path to image file
            data (str): Image data
            cursor (str): The cursor of the image, similar to other tkinter widgets
            anchor (str): The anchor of the image, similar to other tkinter widgets
            relief (str): The relief of the image, similar to other tkinter widgets
            
        Usage:
        
            image = Image(master, file='path to the image file you want to display', anchor='w', relief='groove')
            image.pack()

    """

    def __init__(self, master=None, file=None, data=None, cursor="arrow", anchor="center", relief="flat"):
        
        self._file = file
        self._data = data
        self._cursor = cursor
        self._anchor = anchor
        self._relief = relief
        if self._data != None and self._file is None:
            self.image = tk.PhotoImage(data=self._data)
        elif self._file != None and self._data is None:
            self.image = tk.PhotoImage(file=self._file)
        else:
            raise Exception("Couldn't use file and image data at the same time")
        
        tk.Label.__init__(self, master, image=self.image, cursor=self._cursor, anchor=self._anchor, relief=self._relief)
        
    def cget(self, key):
        """Return the resource value for a KEY given as string"""
        if key is "file":
            return self._text
        elif key is "data":
            return self._extext
        elif key is "cursor":
            return self._cursor
        elif key is "anchor":
            return self._anchor
        elif key is "relief":
            return self._relief
        else:
            raise AttributeError("Image widget has no attribute '" + key + "'")
    
    def keys(self):
        """Return a list of all resource names of this widget"""
        keys = ["file", "data", "cursor", "anchor", "relief"]
        return keys
