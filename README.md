# Tkinter-extension-widgets

## Theme

#### Options:
            
file (str): Path to a tcl theme file\
name (str): The name of the theme\
pkg (str): Path to a folder containing pkgIndex.tcl and other tcl files
            
#### Usage:
        
If you only want to use one of ttk's built-in themes:\
`theme = Theme(root, name='built in theme names e.g.: alt, clam, classic, default, aqua, vista, winnative, xpnative')`

If you want to use a single tcl file (e.g. [azure](https://github.com/rdbende/Azure-ttk-theme)):\
`theme = Theme(root, file='path to a tcl theme file')`
                
If you have a theme package (e.g. [awthemes](https://sourceforge.net/projects/tcl-awthemes/)), you can use it with:\
`theme = Theme(root, pkg='path to a theme package', name='name of theme you want to use')`

## LinkLabel

#### Standard label options:
            
anchor, background, borderwidth, class, compound, cursor, font, foreground, image, justify, padding, relief, state, style, takefocus, text, textvariable, underlinewidth, wraplength
                
#### Specific options:
            
hovercolor (str): Color when you hover the label\
url (str): The link that you want to open\
visited (bool): Sets the link to be visited, it's false by default\
visitedcolor (str): Color after you clicked the label
            
#### Generates:

`<<LinkOpened>>`
            
#### Variable:
        
is_visited = True or False

#### Usage:
        
```bash
link = LinkLabel(master, text='Link', url='https://', hovercolor='#ff0000')
link.pack()
```
                
         
