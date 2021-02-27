"""Simple context / popupmenu for tkinter"""

import tkinter as tk

class PopupMenu(tk.Menu):
    """
        A simple popupmenu for tkinter
        
        Standard menu options:
            
            activebackground, activeborderwidth,
            activeforeground, background, bd, bg
            borderwidth, cursor, disabledforeground
            fg, font, foreground, name, postcommand
            relief, selectcolor, takefocus, tearoff
            tearoffcommand, title, type
                
        Widget-specific options:
            
            relx (int): The X position of the popup relative to the cursor, in pixels
            rely (int): The Y position of the popup relative to the cursor, in pixels
            
        Virtual Event:
        
            <<PopupMenuPopup>>
            
        Usage:
        
            popupmenu = PopupMenu(master)
    """
    
    def __init__(self, master=None, relx=-2, rely=-2, **kwargs):
        self._relx = relx
        self._rely = rely
        kwargs.update({"tearoff" : False})
        tk.Menu.__init__(self, **kwargs)
        self._platform = root.tk.call('tk', 'windowingsystem')
        if self._platform == 'aqua':
            master.bind('<Button-2>', self._popup)
            master.bind('<Control-1>', self._popup)
        else:
            master.bind('<Button-3>', self._popup)

    def _popup(self, event):
        self.event_generate('<<PopupMenuPopup>>')
        try:
            self.tk_popup(int(event.x_root + self._relx), int(event.y_root + self._rely))
        finally:
            self.grab_release()

# Test

if __name__ == '__main__':
    
    root = tk.Tk()
    root.title('PopupMenu')
    root.geometry('250x100')
    
    def callback():
        print('PopupMenu')
    
    popupmenu = PopupMenu(root)
    popupmenu.add_command(label='Command 1', command=callback)
    popupmenu.add_command(label='Command 2', command=callback)
    popupmenu.add_command(label='Command 3', command=callback)
    
    root.mainloop()