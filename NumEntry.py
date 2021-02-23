"""An entry that takes numbers and calculates the result of a calculation"""

import tkinter as tk
from tkinter import ttk
import re

class NumEntry(ttk.Entry):
    """
        An entry that takes numbers and calculates the result of a calculation
        
        Standard entry options:
            
            class, cursor, exportselection
            invalidcommand, justify, show
            state, style, takefocusxscrollcommand
            textvariable, validate, validatecommand, width
                
        Specific options:
            
            expressions (bool): Allow the use of expressions (default is True)
            roundto (bool): The number of decimals in the result
            
        Usage:
        
            numentry = NumEntry(master, roundto=2)
            numentry.pack(pady=20)
    """
    
    def __init__(self, master, expressions=True, roundto=0, **kwargs):
        self._expr = expressions
        self._round = roundto
        ttk.Entry.__init__(self, master, **kwargs)
        self.bind("<Return>", self._eval)
        self.bind("<FocusOut>", self._eval)
        self._old = ""
        self._new = ""

    def _eval(self, *args):
        current = self.get()
        if self._expr:
            try:
                expression = re.sub("[^0-9, +, -, *, /, **, //, %, .]", "", current)
                if self._round == 0:
                    self._new = eval(expression)
                else:
                    self._new = round(float(eval(expression)), self._round)
                self.delete(0, "end")
                self.insert(0, self._new)
                self._old = self._new
            except:
                self.delete(0, "end")
                self.insert(0, self._old)
        else:
            if self._round == 0:
                numbers = re.sub("[^0-9, .]", "", current)
            else:
                numbers = round(float(re.sub("[^0-9, .]", "", current)), self._round)
            self.delete(0, "end")
            self.insert(0, numbers)
        
    def cget(self, key):
        """Return the resource value for a KEY given as string"""
        if key == "expressions":
            return self._expr
        elif key == "roundto":
            return self._round
        else:
            return ttk.Entry.cget(self, key)    
    
    def keys(self):
        """Return a list of all resource names of this widget"""
        keys = ttk.Entry.keys(self)
        keys.extend(["expressions", "roundto"])
        keys = sorted(keys)
        return keys

# Test

if __name__ == '__main__':
    
    root = tk.Tk()
    root.title('NumEntry')
    root.geometry('250x70')
        
    entry = NumEntry(root, expressions=True, roundto=10)
    entry.pack(pady=20)
    
    root.mainloop()
