"""A theme widget for ttk to simply set the main window's theme"""

import tkinter as tk
import tkinter.ttk as ttk
import os.path

class Theme(ttk.Style):
    """
        A theme widget for ttk to simply set the main window's theme
                
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
                self.theme = os.path.basename(self._file).replace(".tcl", "")
            else:
                    self.theme_use(self._name)
                    self.theme = self._name
            
        except Exception:
            raise Exception ("Parent widget must be a root, or a toplevel window!")
        
    def cget(self, key):
        """Return the resource value for a KEY given as string"""
        if key is "name":
            return self._name
        elif key is "file":
            return self._file
        elif key is "pkg":
            return self._pkg
        else:
            raise ValueError("Image widget has no attribute '" + key + "'")
    
    def keys(self):
        """Return a list of all resource names of this widget"""
        keys = ["name", "file", "pkg"]
        return keys
    
# Test

if __name__ == '__main__':

    root = tk.Tk()
    root.title('A theme widget for ttk to simply set the main window\'s theme')
    
    theme = Theme(root, name='clam')
    
    window_height = 530
    window_width = 800

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    options = ['', 'OptionMenu', 'Value 1', 'Value 2']
    a = tk.IntVar()
    b = tk.IntVar()
    b.set(1)
    c = tk.IntVar()
    d = tk.IntVar()
    d.set(2)
    e = tk.StringVar()
    e.set(options[1])
    f = tk.IntVar()
    g = tk.IntVar()
    g.set(75)
    h = tk.IntVar()

    frame1 = ttk.LabelFrame(root, text='Checkbuttons', width=210, height=200)
    frame1.place(x=20, y=12)

    frame2 = ttk.LabelFrame(root, text='Radiobuttons', width=210, height=160)
    frame2.place(x=20, y=252)

    check1 = ttk.Checkbutton(frame1, text='Unchecked', variable=a, offvalue=0, onvalue=1)
    check1.place(x=20, y=20)
    check2 = ttk.Checkbutton(frame1, text='Checked', variable=b, offvalue=0, onvalue=1)
    check2.place(x=20, y=60)
    check3 = ttk.Checkbutton(frame1, text='Third state', variable=c, offvalue=0, onvalue=1)
    check3.state(['alternate'])
    check3.place(x=20, y=100)
    check4 = ttk.Checkbutton(frame1, text='Disabled', state='disabled')
    check4.place(x=20, y=140)

    radio1 = ttk.Radiobutton(frame2, text='Deselected', variable=d, value=1)
    radio1.place(x=20, y=20)
    radio2 = ttk.Radiobutton(frame2, text='Selected', variable=d, value=2)
    radio2.place(x=20, y=60)
    radio3 = ttk.Radiobutton(frame2, text='Disabled', state='disabled')
    radio3.place(x=20, y=100)

    entry = ttk.Entry(root)
    entry.place(x=250, y=20)
    entry.insert(0, 'Entry')

    spin = ttk.Spinbox(root, from_=0, to=100, increment=0.1)
    spin.place(x=250, y=70)
    spin.insert(0, 'Spinbox')

    combo1 = ttk.Combobox(root, value=['Combobox', 'Editable item 1', 'Editable item 2'])
    combo1.current(0)
    combo1.place(x=250, y=120)

    combo2 = ttk.Combobox(root, state='readonly', value=['Readonly combobox', 'Item 1', 'Item 2'])
    combo2.current(0)
    combo2.place(x=250, y=170)

    menu = tk.Menu(root, tearoff=0)
    menu.add_command(label='Menu item 1')
    menu.add_command(label='Menu item 2')
    menu.add_separator()
    menu.add_command(label='Menu item 3')
    menu.add_command(label='Menu item 4')

    menubtn = ttk.Menubutton(root, text='Menubutton', menu=menu, direction='below')
    menubtn.place(x=250, y=220)

    optmenu = ttk.OptionMenu(root, e, *options)
    optmenu.place(x=250, y=270)

    def callback():
        print('Button callback')

    button = ttk.Button(root, text='Button', command=callback)
    button.place(x=250, y=320)

    def scale(i):
        g.set(int(scale.get()))

    scale = ttk.Scale(root, from_=100, to=0, variable=g, command=scale)
    scale.place(x=80, y=430)

    progress = ttk.Progressbar(root, value=0, variable=g, mode='determinate')
    progress.place(x=80, y=480)

    size = ttk.Sizegrip(root)
    size.place(x=780, y=510)

    sep1 = ttk.Separator()
    sep1.place(x=20, y=235, width=210)

    notebook = ttk.Notebook(root)
    notebookTab1 = ttk.Frame(notebook, width=335, height=150)
    notebook.add(notebookTab1, text='Tab 1')
    notebookTab2 = ttk.Frame(notebook, width=335, height=150)
    notebook.add(notebookTab2, text='Tab 2')
    notebookTab3 = ttk.Frame(notebook, width=335, height=150)
    notebook.add(notebookTab3, text='Tab 3')
    notebook.place(x=420, y=330)

    treeFrame = ttk.Frame(root)
    treeFrame.place(x=420, y=20)

    treeScroll = ttk.Scrollbar(treeFrame)
    treeScroll.pack(side='right', fill='y')

    treeview = ttk.Treeview(treeFrame, selectmode="extended", yscrollcommand=treeScroll.set, columns=(1, 2), height=12)
    treeview.pack()

    treeScroll.config(command=treeview.yview)

    treeview.column("#0", width=120)
    treeview.column(1, anchor='w', width=100)
    treeview.column(2, anchor='w', width=100)

    treeview.heading("#0", text="Treeview", anchor='center')
    treeview.heading(1, text="Column 1", anchor='center')
    treeview.heading(2, text="Column 2", anchor='center')

    treeview.insert(parent='', index='end', iid=1, text="Parent", values=("Item 1", "Value 1"))
    treeview.item(1, open=True)
    treeview.insert(parent=1, index='end', iid=2, text="Child", values=("Subitem 1.1", "Value 1.1"))
    treeview.insert(parent=1, index='end', iid=3, text="Child", values=("Subitem 1.2", "Value 1.2"))
    treeview.insert(parent=1, index='end', iid=4, text="Child", values=("Subitem 1.3", "Value 1.3"))
    treeview.insert(parent=1, index='end', iid=5, text="Child", values=("Subitem 1.4", "Value 1.4"))
    treeview.insert(parent='', index='end', iid=6, text="Parent", values=("Item 2", "Value 2"))
    treeview.item(6, open=True)
    treeview.insert(parent=6, index='end', iid=13, text="Child", values=("Subitem 2.1", "Value 2.1"))
    treeview.insert(parent=6, index='end', iid=7, text="Sub-parent", values=("Subitem 2.2", "Value 2.2"))
    treeview.item(7, open=True)
    treeview.insert(parent=7, index='end', iid=8, text="Child", values=("Subitem 2.2.1", "Value 2.2.1"))
    treeview.insert(parent=7, index='end', iid=9, text="Child", values=("Subitem 2.2.2", "Value 2.2.2"))
    treeview.selection_set(9)
    treeview.insert(parent=7, index='end', iid=10, text="Child", values=("Subitem 2.2.3", "Value 2.2.3"))
    treeview.insert(parent=6, index='end', iid=11, text="Child", values=("Subitem 2.3", "Value 2.3"))
    treeview.insert(parent=6, index='end', iid=12, text="Child", values=("Subitem 2.4", "Value 2.4"))
    treeview.insert(parent='', index='end', iid=14, text="Parent", values=("Item 3", "Value 3"))
    treeview.item(14, open=True)
    treeview.insert(parent=14, index='end', iid=15, text="Child", values=("Subitem 3.1", "Value 3.1"))
    treeview.insert(parent=14, index='end', iid=16, text="Child", values=("Subitem 3.2", "Value 3.2"))
    treeview.insert(parent=14, index='end', iid=17, text="Child", values=("Subitem 3.3", "Value 3.3"))
    treeview.insert(parent=14, index='end', iid=18, text="Child", values=("Subitem 3.4", "Value 3.4"))
    treeview.insert(parent='', index='end', iid=19, text="Parent", values=("Item 4", "Value 4"))
    treeview.item(19, open=True)
    treeview.insert(parent=19, index='end', iid=20, text="Child", values=("Subitem 4.1", "Value 4.1"))
    treeview.insert(parent=19, index='end', iid=21, text="Sub-parent", values=("Subitem 4.2", "Value 4.2"))
    treeview.item(21, open=True)
    treeview.insert(parent=21, index='end', iid=22, text="Child", values=("Subitem 4.2.1", "Value 4.2.1"))
    treeview.insert(parent=21, index='end', iid=23, text="Child", values=("Subitem 4.2.2", "Value 4.2.2"))
    treeview.insert(parent=21, index='end', iid=24, text="Child", values=("Subitem 4.2.3", "Value 4.2.3"))
    treeview.insert(parent=19, index='end', iid=25, text="Child", values=("Subitem 4.3", "Value 4.3"))

    root.mainloop()
