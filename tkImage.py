"""
Author: rdbende
License: GNU GPLv3
Copyright (c): 2021 rdbende
"""

import tkinter as tk

class Image(tk.Label):
    """An image display widget for tkinter"""

    def __init__(self, master, **kwargs):
        """
        Create an image
                
        Options:
        
            file (str): path to image file
            data (str): image data URI
            cursor (str): image cursor
            anchor (str): image anchor
            relief (str): image relief
            borderwidth (int): image borderwidth
            
        Methods:
            blank: display a transparent image
            clear: clear the image file and data from the widget, and blanks the image
            copy: return a new PhotoImage with the same image as this widget
            get: return the color (red, green, blue) of the pixel at 'x','y'
            image_names: return the available image names in the program
            image_types: return the available image types in the program
            subsample: return a new PhotoImage based on the same image as this widget
                        but use only every 'x'th or 'y'th pixel. If y is not given, the
                        default value is the same as x
            put: put row formatted colors to image starting from
                    position 'to', e.g. image.put("{red green} {blue yellow}", to=(4,6))
            write: write image to file 'filename' in 'format' starting from
                    position 'form_coords'
            zoom: return a new PhotoImage with the same image as this widget,
                    but zoom it with a factor of x in the 'x' direction and y in the 'y'
                    direction.  If y is not given, the default value is the same as x
        """
        self._file = kwargs.pop("file", None)
        self._data = kwargs.pop("data", None)
        self._cursor = kwargs.pop("cursor", "arrow")
        self._anchor = kwargs.pop("anchor", tk.CENTER)
        self._relief = kwargs.pop("relief", tk.FLAT)
        self._bd = kwargs.pop("borderwidth", 0)
        if self._data is not None and self._file is None:
            self._image = tk.PhotoImage(data=self._data)
        elif self._file is not None and self._data is None:
            self._image = tk.PhotoImage(file=self._file)
        else:
            raise Exception("Couldn't use image file and image data at the same time")
        tk.Label.__init__(self, master, image=self._image, cursor=self._cursor, anchor=self._anchor, relief=self._relief, borderwidth=self._bd)
    
    def __getitem__(self, key):
        return self.cget(key)

    def __setitem__(self, key, value):
        self.configure(**{key: value})
        
    def clear(self):
        """Clear the image file and data from the widget, and blanks the image"""
        self._file = None
        self._data = None
        self._image.blank()
        tk.Label.update(self)
        
    def blank(self):
        """Display a transparent image"""
        self._image.blank()
        
    def copy(self):
        """Return a new PhotoImage with the same image as this widget"""
        return self._image.copy()
    
    def zoom(self, *args, **kwargs):
        """Return a new PhotoImage with the same image as this widget,
        but zoom it with a factor of x in the 'x' direction and y in the 'y'
        direction.  If y is not given, the default value is the same as x"""
        return self._image.zoom(*args, **kwargs)
    
    def subsample(self, *args, **kwargs):
        """Return a new PhotoImage based on the same image as this widget
        but use only every 'x'th or 'y'th pixel. If y is not given, the
        default value is the same as x"""
        return self._image.subsample(*args, **kwargs)
    
    def get(self, *args, **kwargs):
        """Return the color (red, green, blue) of the pixel at 'x','y'"""
        return self._image.get(*args, **kwargs)
    
    def put(self, *args, **kwargs):
        """Put row formatted colors to image starting from
        position 'to', e.g. image.put("{red green} {blue yellow}", to=(4,6))"""
        self._image.put(*args, **kwargs)
        
    def write(self, *args, **kwargs):
        """Write image to file 'filename' in 'format' starting from
        position 'form_coords'"""
        self._image.write(*args, **kwargs)
        
    def image_names(self):
        """Return the available image names in the program"""
        return tk._default_root.tk.splitlist(tk._default_root.tk.call('image', 'names'))

    def image_types(self):
        """Return the available image types in the program"""
        return tk._default_root.tk.splitlist(tk._default_root.tk.call('image', 'types'))
    
    def configure(self, **kwargs):
        """Configure resources of the widget."""
        self._file = kwargs.pop("file", self._file)
        self._data = kwargs.pop("data", self._data)
        self._cursor = kwargs.pop("cursor", self._cursor)
        self._anchor = kwargs.pop("anchor", self._anchor)
        self._relief = kwargs.pop("relief", self._relief)
        self._bd = kwargs.pop("borderwidth", self._bd)
        if self._data is not None and self._file is None:
            self._image = tk.PhotoImage(data=self._data)
        elif self._file is not None and self._data is None:
            self._image = tk.PhotoImage(file=self._file)
        else:
            raise Exception("Couldn't use image file and image data at the same time")
        tk.Label.configure(self, image=self._image, cursor=self._cursor, anchor=self._anchor, relief=self._relief, borderwidth=self._bd)
        
    config = configure
    
    def cget(self, key):
        """Return the resource value for a KEY given as string"""
        if key == "file":
            return self._text
        elif key == "data":
            return self._data
        elif key == "cursor":
            return self._cursor
        elif key == "anchor":
            return self._anchor
        elif key == "relief":
            return self._relief
        elif key == "borderwidth":
            return self._bd
        else:
            raise AttributeError(f"Image widget has no attribute '{key}'")
    
    def keys(self):
        """Return a list of all resource names of this widget"""
        keys = ["anchor", "borderwidth", "cursor", "data", "file", "relief"]
        return keys
