"""A simple menubar for tkinter"""

import tkinter as tk
import _tkinter

class MenuBar(tk.Menu):
    """
        A simple menubar for tkinter
        
        Standard menu options:
            
            activebackground, activeborderwidth,
            activeforeground, background, bd, bg
            borderwidth, cursor, disabledforeground
            fg, font, foreground, name, postcommand
            relief, selectcolor, takefocus, tearoff
            tearoffcommand, title, type
                
        Widget-specific options:
            
            tearoff (bool): Disables / enables tearoff of all menus and submenus (default is False)
            
        Usage:
        
            menubar = MenuBar(master)
            submenu = tk.Menu(menubar)
            menubar.add_cascade(menu=submenu)
    """
    
    def __init__(self, master, tearoff=False, **kwargs):
        tk.Menu.__init__(self, **kwargs)
        master.option_add('*tearOff', tearoff)
        try:
            master.configure(menu=self)
        except _tkinter.TclError:
            raise _tkinter.TclError('The parent of the menubar must be a tk.Tk or tk.Toplevel widget')

# Test

if __name__ == '__main__':
    
    root = tk.Tk()
    root.title('MenuBar')
    root.geometry('250x50')
    
    def callback():
        print('MenuBar')
    
    menubar = MenuBar(root, background='#007fff')
    
    # Testing the Apple menu, and help menu (on X11)
    if root.tk.call('tk', 'windowingsystem') == 'aqua':
        appmenu = tk.Menu(menubar, name='apple')
        menubar.add_cascade(menu=appmenu)
        appmenu.add_command(label='Apple submenu')
    elif root.tk.call('tk', 'windowingsystem') == 'x11':
        helpmenu = tk.Menu(menubar, name='help')
        menubar.add_cascade(menu=helpmenu)
        helpmenu.add_command(label='About')
        
    menu_1 = tk.Menu(menubar)
    menubar.add_cascade(menu=menu_1, label='Submenu 1')
    menu_1.add_command(label='Submenu command', command=callback)
    
    menu_2 = tk.Menu(menubar)
    menubar.add_cascade(menu=menu_2, label='Submenu 2')
    menu_2.add_command(label='Submenu command', command=callback)
    
    menubar.add_command(label='Command', command=callback)  
    
    root.mainloop()
