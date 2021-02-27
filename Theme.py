"""A theme widget for ttk to simply set the main window's theme"""

import tkinter as tk
import tkinter.ttk as ttk
import os.path

class Theme(ttk.Style):
    """
        If you want to change the appearance of you Tkinter window simply you can do so with the theme widget
        
        Options:
            file (str): Path to a tcl theme file
            name (str): The name of the theme
            pkg (str): Path to a folder containing pkgIndex.tcl and other tcl files

        Usage:
            If you only want to use one of ttk's built-in themes (e.g. alt, clam, classic, default, aqua, vista, winnative, xpnative):
                theme = Theme(master, name='theme name')
                
            If you want to use a single tcl file (e.g. azure, breeze, waldorf, or a theme from ttkthemes):
                theme = Theme(master, file='path to a tcl theme file')
        
            If you have a theme package (e.g. awthemes), you can use it with:
                theme = Theme(master, pkg='path to a theme package', name='name of theme you want to use')         
    """

    def __init__(self, master, name=None, file=None, pkg=None):
        self._pkg = pkg
        self._name = name
        self._file = file
        self.master = master
        ttk.Style.__init__(self, master)
        if self._file is not None and self._name is not None:
            raise Exception("Couldn't use theme name and tcl file at the same time")
        
        if self._pkg is not None:
            self.master.tk.call('lappend', 'auto_path', self._pkg)
            self.master.tk.call('package', 'require', os.path.basename(self._name))
            
        if self._file is not None:
            self.master.tk.call('source', self._file)
            self.theme_use(os.path.basename(self._file).replace(".tcl", ""))
        else:
            try:
                self.theme_use(self._name)
            except:
                raise Exception('Something went wrong while setting the theme')
        self.theme = self.theme_use()
        
    def cget(self, key):
        """Return the resource value for a KEY given as string"""
        if key == "file":
            return self._file
        elif key == "name":
            return self._name
        elif key == "pkg":
            return self._pkg
        else:
            raise ValueError("Theme widget has no attribute '" + key + "'")
    
    def keys(self):
        """Return a list of all resource names of this widget"""
        keys = ["file", "name", "pkg"]
        return keys
    
# Test

if __name__ == '__main__':

    root = tk.Tk()
    root.title('Theme widget')
    root.geometry('250x70')
    
    theme = Theme(root, name='classic')
    
    button = ttk.Button(root, text=theme.theme, command=root.destroy)
    button.pack(pady=20)
    
    root.mainloop()
